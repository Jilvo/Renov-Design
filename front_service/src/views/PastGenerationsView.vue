<template>
  <div>
    <Header />
    <div v-if="pastgenerations.length" class="pt-20">
      <div class="flex flex-wrap gap-3 mb-4">
        <span
          v-for="style in styles"
          :key="style"
          @click="filterStyle(style)"
          :class="{
            'bg-blue-600 text-white': style === selectedStyle,
            'bg-gray-200 text-gray-700': style !== selectedStyle
          }"
          class="cursor-pointer px-3 py-1 rounded-full text-sm font-semibold hover:bg-blue-500 hover:text-white transition-colors duration-200"
        >
          {{ style }}
        </span>
        <span
          @click="clearFilter"
          class="cursor-pointer px-3 py-1 bg-gray-400 text-white rounded-full text-sm font-semibold hover:bg-gray-500 transition-colors duration-200"
        >
          Réinitialiser le filtre
        </span>
      </div>

      <HistoryCard
        v-for="(generation, index) in filteredGenerations"
        :key="index"
        :generation="generation"
      />
    </div>
    <div v-else>
      <p>No past generations found.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Header from '../components/Header/Header.vue'
import HistoryCard from '../components/History/HistoryCard.vue'

export default {
  components: {
    Header,
    HistoryCard
  },
  data() {
    return {
      pastgenerations: [],
      styles: [
        'Modern Minimalist Style',
        'Rustic Country Style',
        'Scandinavian Style',
        'Industrial Style',
        'Traditional Style',
        'Art Deco Style',
        'Contemporary Eclectic Style',
        'High-Tech Style',
        'Bohemian Style',
        'Farmhouse Style'
      ],
      styleMapping: {
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
      },
      selectedStyle: null
    }
  },
  computed: {
    filteredGenerations() {
      if (!this.selectedStyle) {
        return this.pastgenerations
      }
      return this.pastgenerations.filter((generation) => {
        const styleName = this.styleMapping[generation.tags]
        return styleName === this.selectedStyle
      })
    }
  },
  methods: {
    async fetchGenerations() {
      try {
        const response = await axios.get('http://localhost:8081/stockage/prompts')
        this.pastgenerations = (response.data.message || response.data).reverse()
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    },
    filterStyle(style) {
      this.selectedStyle = style
    },
    clearFilter() {
      this.selectedStyle = null
    }
  },
  created() {
    this.fetchGenerations()
  }
}
</script>
