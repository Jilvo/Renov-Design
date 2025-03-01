<template>
  <div class="history-card bg-white dark:bg-gray-800 p-8 my-6 rounded-2xl shadow-lg hover:shadow-xl transition-all duration-300">
    <!-- En-tête de la carte -->
    <div class="header text-center mb-6 space-y-2">
      <h3 class="text-xl font-bold bg-gradient-to-r from-green-600 to-green-800 bg-clip-text text-transparent">
        {{ $data[generation.tags] }}
      </h3>
      <p class="text-gray-500 dark:text-gray-400">{{ getDescription(generation.tags) }}</p>
    </div>

    <!-- Conteneur des images -->
    <div class="images-container flex flex-col md:flex-row items-center justify-center gap-6 w-full max-w-[1920px] mx-auto">
      <!-- Image originale -->
      <div class="image-box relative group w-full md:w-1/2">
        <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-all duration-300 rounded-xl"></div>
        <div class="relative bg-gray-50 dark:bg-gray-700 p-4 rounded-xl">
          <img
            v-if="generation.generation_origin"
            :src="generateS3Url(generation.generation_origin)"
            loading="lazy"
            alt="Image originale"
            class="w-full h-[400px] md:h-[600px] object-cover rounded-lg shadow-md transition-transform duration-300 ease-in-out transform group-hover:scale-[1.02]"
          />
          <div class="absolute top-2 left-2 bg-white dark:bg-gray-800 px-3 py-1 rounded-full shadow-md">
            <span class="text-sm font-medium text-gray-600 dark:text-gray-300">Avant</span>
          </div>
        </div>
      </div>

      <!-- Flèche de transition -->
      <div class="transform rotate-90 md:rotate-0">
        <i class="fas fa-long-arrow-alt-right text-3xl text-green-600 dark:text-green-500"></i>
      </div>

      <!-- Image transformée -->
      <div class="image-box relative group w-full md:w-1/2">
        <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-10 transition-all duration-300 rounded-xl"></div>
        <div class="relative bg-gray-50 dark:bg-gray-700 p-4 rounded-xl">
          <img
            v-if="generation.modified_image"
            :src="generateS3Url(generation.modified_image)"
            loading="lazy"
            alt="Image transformée"
            class="w-full h-[400px] md:h-[600px] object-cover rounded-lg shadow-md transition-transform duration-300 ease-in-out transform group-hover:scale-[1.02]"
          />
          <div class="absolute top-2 right-2 bg-green-500 px-3 py-1 rounded-full shadow-md">
            <span class="text-sm font-medium text-white">Après</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Actions -->
    <div class="flex flex-wrap justify-end gap-3 mt-6">
      <button
        @click="showDetails(generation)"
        class="flex items-center gap-2 px-4 py-2 bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 font-medium rounded-xl shadow-sm hover:shadow-md transition-all duration-200"
      >
        <i class="fas fa-info-circle"></i>
        <span>Détails</span>
      </button>
      <button
        @click="shareStyle(generation)"
        class="flex items-center gap-2 px-4 py-2 bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-200 font-medium rounded-xl shadow-sm hover:shadow-md transition-all duration-200"
      >
        <i class="fas fa-share-alt"></i>
        <span>Partager</span>
      </button>
      <button
        @click="saveStyle(generation)"
        class="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-600 to-green-800 text-white font-medium rounded-xl shadow-sm hover:shadow-md transition-all duration-200"
      >
        <i class="fas fa-heart"></i>
        <span>Favoris</span>
      </button>
    </div>

    <!-- Modal de détails -->
    <div
      v-if="isModalVisible"
      class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm"
      @click.self="closeModal"
    >
      <div class="bg-white dark:bg-gray-800 p-8 rounded-2xl shadow-xl max-w-md w-full mx-4 transform transition-all duration-300 scale-100">
        <h2 class="text-2xl font-bold mb-6 bg-gradient-to-r from-green-600 to-green-800 bg-clip-text text-transparent">
          Détails de la transformation
        </h2>
        
        <div class="space-y-4">
          <div class="flex items-center gap-3 text-gray-600 dark:text-gray-300">
            <i class="fas fa-calendar-alt w-6"></i>
            <div>
              <p class="text-sm font-medium">Date de création</p>
              <p class="text-gray-500">{{ formateDate(generation.creation_date) }}</p>
            </div>
          </div>

          <div class="flex items-center gap-3 text-gray-600 dark:text-gray-300">
            <i class="fas fa-user w-6"></i>
            <div>
              <p class="text-sm font-medium">Créé par</p>
              <p class="text-gray-500">{{ generation.created_by }}</p>
            </div>
          </div>

          <div class="flex items-center gap-3 text-gray-600 dark:text-gray-300">
            <i class="fas fa-tag w-6"></i>
            <div>
              <p class="text-sm font-medium">Style</p>
              <p class="text-gray-500">{{ generation.tags }}</p>
            </div>
          </div>

          <div class="flex items-center gap-3 text-gray-600 dark:text-gray-300">
            <i class="fas fa-clock w-6"></i>
            <div>
              <p class="text-sm font-medium">Durée de traitement</p>
              <p class="text-gray-500">{{ generation.processing_duration }} secondes</p>
            </div>
          </div>
        </div>

        <button
          @click="closeModal"
          class="mt-8 w-full px-4 py-3 bg-gradient-to-r from-green-600 to-green-800 text-white font-medium rounded-xl shadow-sm hover:shadow-md transition-all duration-200"
        >
          Fermer
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    generation: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      isModalVisible: false,
      bucketName: 'renov-design',
      basePath: 'https://renov-design.s3.fr-par.scw.cloud',
      0: 'Style Moderne Minimaliste',
      1: 'Style Rustique',
      2: 'Style Scandinave',
      3: 'Style Industriel',
      4: 'Style Traditionnel',
      5: 'Style Art Déco',
      6: 'Style Contemporain',
      7: 'Style High-Tech',
      8: 'Style Bohème',
      9: 'Style Champêtre'
    }
  },
  methods: {
    generateS3Url(path) {
      return `${this.basePath}/${this.bucketName}/${path}`
    },
    getDescription(tag) {
      const descriptions = {
        'Style Moderne Minimaliste': 'Épuré et fonctionnel, axé sur la simplicité.',
        'Style Rustique': 'Chaleureux et authentique, matériaux naturels.',
        'Style Scandinave': 'Lumineux et fonctionnel, inspiration nordique.',
        'Style Industriel': 'Brut et urbain, matériaux métalliques.',
        'Style Traditionnel': 'Élégant et intemporel, touches classiques.',
        'Style Art Déco': 'Luxueux et géométrique, inspiration années 20.',
        'Style Contemporain': 'Actuel et éclectique, mélange harmonieux.',
        'Style High-Tech': 'Innovant et futuriste, technologie intégrée.',
        'Style Bohème': 'Artistique et libre, mélange de couleurs et textures.',
        'Style Champêtre': 'Naturel et romantique, inspiration campagne.'
      }
      return descriptions[tag] || 'Une transformation unique de votre intérieur.'
    },
    shareStyle(generation) {
      if (navigator.share) {
        navigator.share({
          title: 'Ma transformation d\'intérieur',
          text: `Découvrez ma transformation en style ${generation.tags}`,
          url: window.location.href
        })
      } else {
        // Fallback pour les navigateurs qui ne supportent pas l'API Web Share
        alert('Fonctionnalité de partage non disponible sur ce navigateur')
      }
    },
    saveStyle(generation) {
      // TODO: Implémenter la sauvegarde dans les favoris
      alert('Transformation ajoutée aux favoris !')
    },
    showDetails(generation) {
      this.isModalVisible = true
    },
    closeModal() {
      this.isModalVisible = false
    },
    formateDate(date) {
      return new Date(date).toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    }
  }
}
</script>

<style scoped>
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}

/* Effet de flou sur l'arrière-plan des images */
.image-box::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.02) 100%);
  pointer-events: none;
  border-radius: 0.75rem;
}

/* Animation subtile au hover des boutons */
button {
  transform: translateY(0);
  transition: transform 0.2s ease;
}

button:hover {
  transform: translateY(-1px);
}

button:active {
  transform: translateY(0);
}
</style>
