<template>
  <section class="min-h-screen bg-gradient-to-br from-green-50 to-green-100 dark:from-gray-900 dark:to-gray-800">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto min-h-screen lg:py-0">
      <div
        class="w-full bg-white rounded-2xl shadow-lg md:mt-0 sm:max-w-2xl xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-6 md:space-y-8 sm:p-8">
          <h1
            class="text-2xl font-bold leading-tight tracking-tight bg-gradient-to-r from-green-600 to-green-800 bg-clip-text text-transparent md:text-3xl text-center"
          >
            Transformez votre intérieur
          </h1>

          <form class="space-y-6" @submit.prevent="submitForm">
            <!-- Zone de drop pour l'image -->
            <div
              class="relative border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-xl p-8 text-center cursor-pointer transition-all duration-300 hover:border-green-500 dark:hover:border-green-400"
              :class="{ 'border-green-500': isDragging }"
              @dragenter.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @dragover.prevent
              @drop.prevent="handleDrop"
              @click="$refs.fileInput.click()"
            >
              <input
                type="file"
                ref="fileInput"
                class="hidden"
                accept="image/*"
                @change="handleFileSelect"
                id="file"
                required
              />
              
              <div v-if="!selectedFile" class="space-y-4">
                <i class="fas fa-cloud-upload-alt text-4xl text-gray-400"></i>
                <p class="text-gray-600 dark:text-gray-300">
                  Glissez votre photo ici ou cliquez pour sélectionner
                </p>
                <p class="text-sm text-gray-400">Format accepté : JPG, PNG (max 10MB)</p>
              </div>

              <div v-else class="relative">
                <img
                  :src="imagePreview"
                  alt="Aperçu"
                  class="max-h-64 mx-auto rounded-lg shadow-md"
                />
                <button
                  type="button"
                  @click.stop="removeFile"
                  class="absolute top-2 right-2 bg-red-500 text-white rounded-full p-2 hover:bg-red-600 transition-colors duration-200"
                >
                  <i class="fas fa-times"></i>
                </button>
              </div>
            </div>

            <!-- Sélection du style -->
            <div class="space-y-4">
              <label class="block text-lg font-medium text-gray-900 dark:text-white mb-4">
                Choisissez votre style
              </label>
              <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                <button
                  v-for="style in styles"
                  :key="style.id"
                  type="button"
                  class="p-4 rounded-xl border-2 transition-all duration-200 flex flex-col items-center gap-2"
                  :class="[
                    selectedStyleId === style.id
                      ? 'border-green-500 bg-green-50 dark:bg-green-900'
                      : 'border-gray-200 hover:border-green-300 dark:border-gray-600',
                  ]"
                  @click="selectStyle(style.id)"
                >
                  <i :class="['fas', style.icon, 'text-2xl', selectedStyleId === style.id ? 'text-green-600' : 'text-gray-600']"></i>
                  <span class="text-sm font-medium" :class="selectedStyleId === style.id ? 'text-green-700 dark:text-green-400' : 'text-gray-700 dark:text-gray-300'">
                    {{ style.name }}
                  </span>
                </button>
              </div>
            </div>

            <!-- Bouton de soumission -->
            <button
              type="submit"
              :disabled="!canSubmit"
              class="w-full text-white bg-gradient-to-r from-green-600 to-green-800 hover:from-green-700 hover:to-green-900 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-xl text-sm px-5 py-4 text-center transform transition-all duration-200 ease-in-out hover:scale-[1.02] hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
            >
              <span v-if="isLoading" class="flex items-center justify-center">
                <i class="fas fa-spinner fa-spin mr-2"></i>
                Transformation en cours...
              </span>
              <span v-else>
                Transformer ma pièce
              </span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      selectedFile: null,
      imagePreview: null,
      isDragging: false,
      isLoading: false,
      selectedStyleId: null,
      styles: [
        { id: 0, name: 'Moderne', icon: 'fa-building' },
        { id: 1, name: 'Rustique', icon: 'fa-home' },
        { id: 2, name: 'Scandinave', icon: 'fa-snowflake' },
        { id: 3, name: 'Industriel', icon: 'fa-industry' },
        { id: 4, name: 'Traditionnel', icon: 'fa-landmark' },
        { id: 5, name: 'Art Déco', icon: 'fa-gem' },
        { id: 6, name: 'Contemporain', icon: 'fa-vector-square' },
        { id: 7, name: 'High-Tech', icon: 'fa-microchip' },
        { id: 8, name: 'Bohème', icon: 'fa-leaf' },
        { id: 9, name: 'Champêtre', icon: 'fa-tree' }
      ]
    }
  },
  computed: {
    canSubmit() {
      return this.selectedFile && this.selectedStyleId !== null && !this.isLoading
    }
  },
  methods: {
    handleDrop(e) {
      this.isDragging = false
      const file = e.dataTransfer.files[0]
      this.processFile(file)
    },
    handleFileSelect(e) {
      const file = e.target.files[0]
      this.processFile(file)
    },
    processFile(file) {
      if (file && file.type.startsWith('image/')) {
        if (file.size <= 10 * 1024 * 1024) { // 10MB max
          this.selectedFile = file
          const reader = new FileReader()
          reader.onload = e => {
            this.imagePreview = e.target.result
          }
          reader.readAsDataURL(file)
        } else {
          alert('L\'image ne doit pas dépasser 10MB')
        }
      } else {
        alert('Veuillez sélectionner une image valide')
      }
    },
    removeFile() {
      this.selectedFile = null
      this.imagePreview = null
      this.$refs.fileInput.value = ''
    },
    selectStyle(styleId) {
      this.selectedStyleId = styleId
    },
    async submitForm() {
      if (!this.canSubmit) return

      const formData = new FormData()
      formData.append('file', this.selectedFile)
      formData.append('styleName', this.selectedStyleId)
      formData.append('userId', '1000')

      try {
        this.isLoading = true
        const response = await axios.post('http://localhost:9000/modify', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log('Upload successful:', response.data)
        // Redirection ou autre traitement après succès
      } catch (error) {
        console.error('Upload failed:', error)
        alert('Une erreur est survenue lors de la transformation')
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

section {
  animation: fadeIn 0.5s ease-out;
}

.group:focus-within label {
  color: #059669;
}

button:not(:disabled):active {
  transform: scale(0.98);
}

/* Animation pour le drag & drop */
@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.02);
  }
  100% {
    transform: scale(1);
  }
}

.border-dashed.border-green-500 {
  animation: pulse 1s infinite;
}

/* Animation du spinner */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.fa-spinner {
  animation: spin 1s linear infinite;
}
</style>
