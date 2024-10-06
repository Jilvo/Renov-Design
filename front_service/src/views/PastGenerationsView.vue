<template>
  <div>
    <Header />
    <div v-if="pastgenerations.length" class="pt-52">
      <HistoryCard
        v-for="(generation, index) in pastgenerations"
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
    // eslint-disable-next-line vue/no-reserved-component-names
    Header,
    HistoryCard
  },
  data() {
    return {
      pastgenerations: []
    }
  },
  methods: {
    async fetchGenerations() {
      console.log('fetchGenerations called')
      try {
        const response = await axios.get('http://localhost:8081/stockage/prompts')
        console.log('Raw data fetched:', response.data)
        this.pastgenerations = (response.data.message || response.data).reverse()
        console.log('Data assigned to pastgenerations:', this.pastgenerations)
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    }
  },
  created() {
    console.log('Component created')
    this.fetchGenerations()
  }
}
</script>
docker run -p 8081:8081 stockage_service
