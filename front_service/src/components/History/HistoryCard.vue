<template>
  <div class="history-card border border-gray-300 p-6 my-4 rounded-lg shadow-lg">
    <div class="header text-center mb-4">
      <strong>{{ $data[generation.tags] }}</strong> <br />
      <span class="text-gray-500">{{ getDescription(generation.tags) }}</span>
      <!-- <strong>{{ generation.processing_duration }} seconds</strong> -->
    </div>
    <div class="images-container flex items-center justify-center">
      <div class="image-box border border-gray-300 p-2 mx-2">
        <img
          v-if="generation.generation_origin"
          :src="generateS3Url(generation.generation_origin)"
          loading="lazy"
          alt="Original Image from S3"
          class="s3-image max-w-96 h-96 transition-transform duration-300 ease-in-out transform hover:scale-105"
        />
        <p class="text-center text-gray-600 mt-2">{{ $data[generation.tags] }} - Avant</p>
      </div>
      <div class="arrow text-2xl mx-2">➔</div>
      <div class="image-box border border-gray-300 p-2 mx-2">
        <img
          v-if="generation.modified_image"
          :src="generateS3Url(generation.modified_image)"
          loading="lazy"
          alt="Modified Image from S3"
          class="s3-image max-w-96 h-96 transition-transform duration-300 ease-in-out transform hover:scale-105"
        />
        <p class="text-center text-gray-600 mt-2">{{ $data[generation.tags] }} - Après</p>
      </div>
    </div>
    <div class="flex justify-end space-x-2 mt-4">
      <button
        @click="showDetails(generation)"
        class="px-4 py-2 bg-white bg-opacity-30 backdrop-blur-sm text-indigo-600 font-semibold rounded-lg shadow-md hover:bg-opacity-50 transition duration-200 ease-in-out"
      >
        Voir les détails
      </button>
      <button
        @click="shareStyle(generation)"
        class="px-4 py-2 bg-white bg-opacity-30 backdrop-blur-sm text-green-600 font-semibold rounded-lg shadow-md hover:bg-opacity-50 transition duration-200 ease-in-out"
      >
        Partager
      </button>
      <button
        @click="saveStyle(generation)"
        class="px-4 py-2 bg-white bg-opacity-30 backdrop-blur-sm text-yellow-600 font-semibold rounded-lg shadow-md hover:bg-opacity-50 transition duration-200 ease-in-out"
      >
        Favoris
      </button>
    </div>

    <!-- Popup (Modale) -->
    <div
      v-if="isModalVisible"
      class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75"
    >
      <div class="bg-white p-6 rounded-lg shadow-lg text-left max-w-sm">
        <h2 class="text-xl font-semibold mb-4">Détails de la génération</h2>
        <!-- <p><strong>ID:</strong> {{ generation.id }}</p> -->
        <p><strong>Création:</strong> {{ formateDate(generation.creation_date) }}</p>
        <p><strong>Créé par:</strong> {{ generation.created_by }}</p>
        <p><strong>Tags:</strong> {{ generation.tags }}</p>
        <p><strong>Status:</strong> {{ generation.status }}</p>
        <p><strong>Durée:</strong> {{ generation.processing_duration }} seconds</p>
        <!-- Ajoutez d'autres propriétés si nécessaire -->
        <button
          @click="closeModal"
          class="mt-4 px-4 py-2 bg-white bg-opacity-30 backdrop-blur-sm text-red-600 font-semibold rounded-lg shadow-md hover:bg-opacity-50 transition duration-200 ease-in-out"
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
      isModalVisible: false, // État de visibilité de la modale
      bucketName: 'renov-design',
      basePath: 'https://s3.fr-par.scw.cloud',
      0: 'Modern Minimalist Style',
      1: 'Rustic Country Style',
      2: 'Scandinavian Style',
      3: 'Industrial Style',
      4: 'Traditional Style',
      5: 'Art Deco Style',
      6: 'Contemporary Eclectic Style',
      7: 'High-Tech Style',
      8: 'Bohemian Style',
      9: 'Farmhouse Style'
    }
  },
  methods: {
    generateS3Url(path) {
      return `${this.basePath}/${this.bucketName}/${path}`
    },
    getDescription(tag) {
      const descriptions = {
        'Industrial Style': 'Un style brut avec des matériaux industriels.',
        'Art Deco Style': 'Un style élégant inspiré des années 1920.'
        // Ajouter les autres descriptions selon les styles
      }
      return descriptions[tag] || ''
    },
    shareStyle(generation) {
      // Implémentation du partage via Web Share API ou autre
    },
    saveStyle(generation) {
      // Implémentation de la sauvegarde (local storage ou API)
    },
    showDetails(generation) {
      this.isModalVisible = true // Affiche la modale
    },
    closeModal() {
      this.isModalVisible = false // Cache la modale
    },
    formateDate(date) {
      return new Date(date).toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    }
  },
  created() {
    console.log('HistoryCard created with generation:', this.generation)
  }
}
</script>

<style scoped>
.arrow {
  font-size: 24px;
}
</style>
