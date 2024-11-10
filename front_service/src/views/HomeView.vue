<template>
  <Header />
  <body class="font-body">
    <!-- home section -->
    <section class="bg-white mb-20 md:mb-52 xl:mb-72">
      <div class="container max-w-screen-xl mx-auto px-4">
        <div class="flex items-center justify-center xl:justify-start">
          <div class="mt-28 text-center xl:text-left">
            <h1 class="font-semibold text-4xl md:text-6xl lg:text-7xl text-gray-900 leading-normal mb-6">
              Get your dream <br />
              house now
            </h1>
            <p class="font-normal text-xl text-gray-400 leading-relaxed mb-12">
              You want to restyle a room in your house ?<br />
              We offer you a wide range of styles to choose from.
            </p>
            <button class="px-6 py-4 bg-green-700 text-white font-semibold text-lg rounded-xl hover:bg-green-900 transition ease-in-out duration-500">
              Create a new style now
            </button>
          </div>
          <div class="hidden xl:block xl:absolute z-0 top-0 right-0">
            <img :src="homeimg" alt="Home img" />
          </div>
        </div>
      </div>
    </section>

    <!-- gallery section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4">
        <h1 class="font-semibold text-gray-900 text-4xl text-center mb-10">Our Gallery</h1>

        <!-- Filtres de catégories -->
        <div class="flex justify-center space-x-4 mb-8">
          <button @click="filterCategory(null)" :class="{'bg-green-800 text-white': selectedCategory === null}" class="px-6 py-2 font-semibold text-xl rounded-lg hover:bg-green-600 transition ease-in-out duration-500">
            All
          </button>
          <button @click="filterCategory('Industrial Style')" :class="{'bg-green-800 text-white': selectedCategory === 'Industrial Style'}" class="px-6 py-2 font-semibold text-xl rounded-lg hover:bg-green-600 transition ease-in-out duration-500">
            Industrial Style
          </button>
          <button @click="filterCategory('Traditional Style')" :class="{'bg-green-800 text-white': selectedCategory === 'Traditional Style'}" class="px-6 py-2 font-semibold text-xl rounded-lg hover:bg-green-600 transition ease-in-out duration-500">
            Traditional Style
          </button>
          <button @click="filterCategory('Farmhouse Style')" :class="{'bg-green-800 text-white': selectedCategory === 'Farmhouse Style'}" class="px-6 py-2 font-semibold text-xl rounded-lg hover:bg-green-600 transition ease-in-out duration-500">
            Farmhouse Style
          </button>
        </div>

        <!-- Images filtrées -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div v-for="image in filteredImages" :key="image.src">
            <img :src="image.src" :alt="image.alt" class="mb-4 hover:opacity-75 transition ease-in-out duration-500" />
          </div>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
import Header from '../components/Header/Header.vue'
import homeimg from '@/assets/images/home-img.png'
import gallery1 from '@/assets/images/gallery-1.png'
import gallery2 from '@/assets/images/gallery-2.png'
import gallery3 from '@/assets/images/gallery-3.png'
import gallery4 from '@/assets/images/gallery-4.png'
import gallery5 from '@/assets/images/gallery-5.png'
import gallery6 from '@/assets/images/gallery-6.png'
import gallery7 from '@/assets/images/gallery-7.png'

export default {
  components: {
    Header
  },
  data() {
    return {
      homeimg: homeimg,
      selectedCategory: null, // Par défaut, aucune catégorie n'est sélectionnée

      // Tableau des images avec les catégories associées
      images: [
        { src: gallery1, alt: 'Gallery Image 1', category: 'Industrial Style' },
        { src: gallery2, alt: 'Gallery Image 2', category: 'Traditional Style' },
        { src: gallery3, alt: 'Gallery Image 3', category: 'Farmhouse Style' },
        { src: gallery4, alt: 'Gallery Image 4', category: 'Industrial Style' },
        { src: gallery5, alt: 'Gallery Image 5', category: 'Traditional Style' },
        { src: gallery6, alt: 'Gallery Image 6', category: 'Farmhouse Style' },
        { src: gallery7, alt: 'Gallery Image 7', category: 'Industrial Style' }
      ]
    }
  },
  computed: {
    filteredImages() {
      if (!this.selectedCategory) {
        return this.images // Affiche toutes les images si aucune catégorie n'est sélectionnée
      }
      return this.images.filter(image => image.category === this.selectedCategory)
    }
  },
  methods: {
    filterCategory(category) {
      this.selectedCategory = category
    }
  }
}
</script>

<style scoped>
.button-active {
  background-color: #276749;
  color: white;
}
</style>
