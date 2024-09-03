<template>
  <div>
    <section class="bg-gray-50 dark:bg-gray-900">
      <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto lg:py-0">
        <div
          class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-2xl xl:p-0 dark:bg-gray-800 dark:border-gray-700"
        >
          <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
            <h1
              class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white"
            >
              Upload and Generate Image
            </h1>
            <form @submit.prevent="submitForm" class="space-y-4 md:space-y-6">
              <file-upload
                class="file-uploader"
                ref="uploader"
                v-model="files"
                :multiple="false"
                :drop="true"
                :drop-directory="true"
                post-action="/path/to/upload"
                @input-file="handleFileUpload"
                :extensions="['jpg', 'jpeg', 'png']"
              >
                Drag your file here or click to upload
              </file-upload>
              <div class="grid grid-cols-3 gap-4">
                <template v-for="style in styles" :key="style.id">
                  <button
                    type="button"
                    :style="{ backgroundImage: 'url(' + style.imageUrl + ')' }"
                    @click="selectStyle(style.id)"
                    class="w-32 h-32 bg-cover bg-center rounded-lg focus:outline-none"
                  >
                    {{ style.name }}
                  </button>
                </template>
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
  </div>
</template>

<script>
// import FileUpload from 'vue-upload-component'
// Import image paths are correct and accessible
export default {
  // components: {
  //   FileUpload
  // },
  data() {
    return {
      files: [],
      selectedFile: null,
      selectedStyleId: null,
      styles: [
        // Style definitions with proper image paths
      ]
    }
  },
  methods: {
    handleFileUpload(files) {
      if (files.length > 0) {
        this.selectedFile = files[0].file // Assign the first file as selected
      }
    },
    selectStyle(styleId) {
      this.selectedStyleId = styleId
    },
    submitForm() {
      if (!this.selectedFile || !this.selectedStyleId) {
        alert('Please select an image and a style.')
        return
      }
      console.log('Form submitted with:', this.selectedFile, 'and style', this.selectedStyleId)
      // Further processing can be done here
    }
  }
}
</script>

<style>
button:focus {
  outline: none;
}
.file-uploader {
  border: 2px dashed #ccc;
  padding: 20px;
  text-align: center;
}
</style>
