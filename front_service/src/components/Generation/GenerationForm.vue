<template>
  <section class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center py-8 px-4 md:px-6">
    <div class="w-full max-w-6xl bg-white rounded-lg shadow dark:border dark:bg-gray-800 dark:border-gray-700">
      <div class="p-6 space-y-4 md:space-y-6">
        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center">
          Upload and Generate Image
        </h1>
        
        <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6">
          
          <!-- Zone de drag-and-drop améliorée -->
          <div>
            <label for="file" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              Select an image
            </label>
            <div
              @dragover.prevent
              @drop.prevent="handleFileDrop"
              :class="[
                'file-input relative flex items-center justify-center w-full h-32 border-2 border-dashed rounded-lg cursor-pointer transition-all duration-200',
                selectedFile ? 'border-green-500' : 'hover:border-blue-500',
                'bg-gray-50 dark:bg-gray-700 dark:border-gray-600'
              ]"
            >
              <input
                type="file"
                id="file"
                @change="handleFileChange"
                accept=".jpg,.jpeg,.png"
                class="absolute inset-0 opacity-0"
                required
              />
              <div class="flex flex-col items-center text-gray-500 dark:text-gray-300">
                <svg class="w-10 h-10 mb-3" fill="currentColor" viewBox="0 0 20 20">
                  <path
                    fill-rule="evenodd"
                    d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm4 3a1 1 0 000 2h4a1 1 0 100-2H8z"
                    clip-rule="evenodd"
                  />
                </svg>
                <span v-if="!selectedFile" class="text-sm font-medium">Drag & Drop or Click to Select</span>
                <span v-else class="text-sm font-medium text-green-500">File Selected: {{ selectedFile.name }}</span>
              </div>
            </div>
          </div>

          <!-- Sélection du style améliorée et responsive -->
          <div>
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
              Select a style
            </label>
            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 2xl:grid-cols-5 gap-4">
              <template v-for="style in styles" :key="style.id">
                <div class="group relative">
                  <p
                    :class="{
                      'text-left text-gray-700 dark:text-gray-300 transition-all duration-300': true,
                      'font-bold': style.id === selectedStyleId,
                      'hover:font-bold': style.id !== selectedStyleId
                    }"
                  >
                    {{ style.name }}
                  </p>
                  <button
                    type="button"
                    @click="selectStyle(style.id)"
                    :style="{ backgroundImage: 'url(' + style.imageUrl + ')' }"
                    :class="{
                      'w-28 h-28 md:w-32 md:h-32 bg-cover bg-center rounded-lg transition-all duration-300 transform': true,
                      'border-4 border-blue-500 shadow-lg scale-105': style.id === selectedStyleId,
                      'border-2 border-transparent hover:border-gray-300 hover:scale-105 hover:shadow-md': style.id !== selectedStyleId
                    }"
                  >
                    <span class="sr-only">{{ style.name }}</span>
                  </button>
                </div>
              </template>
            </div>
          </div>

          <!-- Bouton Generate -->
          <button
            type="submit"
            class="w-full text-white bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 transform transition duration-300 ease-in-out hover:scale-105"
          >
            Generate
          </button>

        </form>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

// Import des images ici
import bgButton0 from '@/assets/images/background/0.png'
import bgButton1 from '@/assets/images/background/1.png'
import bgButton2 from '@/assets/images/background/2.png'
import bgButton3 from '@/assets/images/background/3.png'
import bgButton4 from '@/assets/images/background/4.png'
import bgButton5 from '@/assets/images/background/5.png'
import bgButton6 from '@/assets/images/background/6.png'
import bgButton7 from '@/assets/images/background/7.png'
import bgButton8 from '@/assets/images/background/8.png'
import bgButton9 from '@/assets/images/background/9.png'

export default {
  data() {
    return {
      selectedFile: null,
      selectedStyleId: null,
      styles: [
        { id: 0, name: 'Modern Minimalist Style', imageUrl: bgButton0 },
        { id: 1, name: 'Rustic Country Style', imageUrl: bgButton1 },
        { id: 2, name: 'Scandinavian Style', imageUrl: bgButton2 },
        { id: 3, name: 'Industrial Style', imageUrl: bgButton3 },
        { id: 4, name: 'Traditional Style', imageUrl: bgButton4 },
        { id: 5, name: 'Art Deco Style', imageUrl: bgButton5 },
        { id: 6, name: 'Contemporary Eclectic Style', imageUrl: bgButton6 },
        { id: 7, name: 'High-Tech Style', imageUrl: bgButton7 },
        { id: 8, name: 'Bohemian Style', imageUrl: bgButton8 },
        { id: 9, name: 'Farmhouse Style', imageUrl: bgButton9 }
      ]
    }
  },
  methods: {
    handleFileChange(event) {
      const file = event.target.files[0]
      if (file) {
        this.selectedFile = file
      }
    },
    handleFileDrop(event) {
      const file = event.dataTransfer.files[0]
      if (file) {
        this.selectedFile = file
      }
    },
    selectStyle(styleId) {
      this.selectedStyleId = styleId
    },
    async submitForm() {
      if (!this.selectedFile || !this.selectedStyleId) {
        alert('Please select an image and a style.')
        return
      }

      const selectedStyle = this.styles.find((style) => style.id === this.selectedStyleId)

      const formData = new FormData()
      formData.append('file', this.selectedFile)
      formData.append('styleName', selectedStyle.id)
      const user_id = localStorage.getItem('user_id')
      formData.append('userId', user_id)
      // Modify Image
      try {
        const response = await axios.post('http://localhost:5000/modify', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log('Upload successful:', response.data)
      } catch (error) {
        console.error('Upload failed:', error)
      }
    }
  }
}
</script>

<style scoped>
.file-input {
  transition: border-color 0.3s ease, background-color 0.3s ease;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.file-input:hover {
  border-color: #4a90e2;
}

.file-input:active {
  background-color: rgba(74, 144, 226, 0.1);
}

.file-input:focus-within {
  border-color: #4a90e2;
  background-color: rgba(74, 144, 226, 0.05);
}
</style>
