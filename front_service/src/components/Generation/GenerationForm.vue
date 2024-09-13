<template>
  <section class="bg-gray-50 dark:bg-gray-900">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div
        class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-2xl xl:max-w-3xl xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
          >
            Upload and Generate Image
          </h1>
          <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6">
            <div>
              <label for="file" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Select an image</label
              >
              <input
                type="file"
                id="file"
                @change="handleFileChange"
                accept=".jpg,.jpeg,.png"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required
              />
            </div>
            <div>
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                Select a style
              </label>
              <div class="grid grid-cols-3 gap-4">
                <template v-for="style in styles" :key="style.id">
                  <div>
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
                        'w-32 h-32 bg-cover bg-center rounded-lg transition-all duration-300': true,
                        'hover:text-xl': style.id !== selectedStyleId,
                        'active:text-2xl': style.id === selectedStyleId
                      }"
                    >
                      <span class="sr-only">{{ style.name }}</span>
                    </button>
                  </div>
                </template>
              </div>
            </div>
            <button
              type="submit"
              class="w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Generate
            </button>
          </form>
        </div>
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
      formData.append('userId', '1000')
      // Modify Image
      try {
        const response = await axios.post('http://127.0.0.1:5000/modify', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        console.log('Upload successful:')
        console.log('Upload successful:', response.data)
        // Traitez la réponse ici
      } catch (error) {
        console.error('Upload failed:', error)
        // Gérer les erreurs ici
      }
      // Stock information in the database
    }
  }
}
</script>

<style>
button:focus {
  outline: none;
}
.file-input {
  display: block;
  width: 100%;
  padding: 1rem;
  border: 2px dashed #ccc;
  border-radius: 0.5rem;
  text-align: center;
  cursor: pointer;
}

.file-input:hover {
  border-color: #999;
}

/* Additional Styles for Text Size */
p.hover\:text-lg:hover {
  font-size: 1.125rem;
}
button.hover\:text-xl:hover span {
  font-size: 1.25rem;
}
button.active\:text-2xl:active span {
  font-size: 1.5rem;
}
</style>
