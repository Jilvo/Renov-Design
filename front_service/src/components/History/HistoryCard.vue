<template>
  <div class="history-card border border-gray-300 p-4 my-2">
    <div class="header text-center mb-4">
      <strong>{{ $data[generation.tags] }}</strong> <br />
      <strong>{{ generation.processing_duration }} seconds</strong>
    </div>
    <div class="images-container flex items-center justify-center">
      <div class="image-box border border-gray-300 p-2 mx-2">
        <img
          v-if="generation.generation_origin"
          :src="generateS3Url(generation.generation_origin)"
          alt="Original Image from S3"
          class="s3-image max-w-96 h-96"
        />
      </div>
      <div class="arrow text-2xl mx-2">➔</div>
      <div class="image-box border border-gray-300 p-2 mx-2">
        <img
          v-if="generation.modified_image"
          :src="generateS3Url(generation.modified_image)"
          alt="Modified Image from S3"
          class="s3-image max-w-96 h-96"
        />
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
