<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 to-green-100 dark:from-gray-900 dark:to-gray-800">
    <Header />
    
    <div class="container mx-auto px-4 py-8">
      <!-- En-tête de la page -->
      <div class="text-center mb-12 pt-20">
        <h1 class="text-3xl md:text-4xl font-bold bg-gradient-to-r from-green-600 to-green-800 bg-clip-text text-transparent mb-4">
          Mes transformations
        </h1>
        <p class="text-gray-600 dark:text-gray-400">
          Retrouvez l'historique de vos transformations d'intérieur
        </p>
      </div>

      <!-- Barre d'outils -->
      <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-lg p-6 mb-8">
        <div class="flex flex-col md:flex-row gap-6 items-center justify-between">
          <!-- Filtres -->
          <div class="w-full md:w-auto">
            <div class="flex flex-wrap gap-3">
              <button
                v-for="style in styles"
                :key="style"
                @click="filterStyle(style)"
                :class="[
                  'px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200 transform hover:scale-105',
                  style === selectedStyle
                    ? 'bg-gradient-to-r from-green-600 to-green-800 text-white shadow-lg'
                    : 'bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
                ]"
              >
                {{ style }}
              </button>
              <button
                v-if="selectedStyle"
                @click="clearFilter"
                class="px-4 py-2 rounded-xl text-sm font-medium bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-300 hover:bg-red-200 dark:hover:bg-red-800 transition-all duration-200 transform hover:scale-105"
              >
                <i class="fas fa-times mr-2"></i>
                Réinitialiser
              </button>
            </div>
          </div>

          <!-- Options d'affichage -->
          <div class="flex items-center gap-4">
            <div class="flex items-center gap-2 text-gray-600 dark:text-gray-400">
              <span class="text-sm">Trier par:</span>
              <select 
                v-model="sortOption"
                class="bg-gray-100 dark:bg-gray-700 border-0 rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-green-500"
              >
                <option value="date-desc">Plus récent</option>
                <option value="date-asc">Plus ancien</option>
                <option value="duration">Durée</option>
              </select>
            </div>
            
            <div class="flex gap-2">
              <button
                @click="viewMode = 'grid'"
                :class="[
                  'p-2 rounded-lg transition-all duration-200',
                  viewMode === 'grid'
                    ? 'bg-green-100 dark:bg-green-900 text-green-600 dark:text-green-400'
                    : 'text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'
                ]"
              >
                <i class="fas fa-th-large"></i>
              </button>
              <button
                @click="viewMode = 'list'"
                :class="[
                  'p-2 rounded-lg transition-all duration-200',
                  viewMode === 'list'
                    ? 'bg-green-100 dark:bg-green-900 text-green-600 dark:text-green-400'
                    : 'text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700'
                ]"
              >
                <i class="fas fa-list"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Message de chargement -->
      <div v-if="loading" class="flex justify-center items-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-4 border-green-600 border-t-transparent"></div>
      </div>

      <!-- Message d'erreur -->
      <div v-else-if="error" class="bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-300 p-4 rounded-xl text-center">
        {{ error }}
      </div>

      <!-- Contenu principal -->
      <div v-else>
        <!-- Message si aucune génération -->
        <div v-if="!filteredGenerations.length" class="text-center py-12">
          <i class="fas fa-image text-6xl text-gray-300 dark:text-gray-600 mb-4"></i>
          <p class="text-gray-500 dark:text-gray-400">
            {{ selectedStyle ? 'Aucune transformation trouvée pour ce style.' : 'Aucune transformation trouvée.' }}
          </p>
          <button
            v-if="selectedStyle"
            @click="clearFilter"
            class="mt-4 px-6 py-2 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-colors duration-200"
          >
            Voir toutes les transformations
          </button>
        </div>

        <!-- Liste des générations -->
        <div
          :class="{
            'grid grid-cols-1 gap-8': viewMode === 'grid',
            'space-y-8': viewMode === 'list'
          }"
        >
          <TransitionGroup
            name="list"
            tag="div"
            :class="{ 'space-y-8': viewMode === 'list' }"
          >
            <HistoryCard
              v-for="generation in sortedGenerations"
              :key="generation.id"
              :generation="generation"
              :view-mode="viewMode"
              class="w-full"
            />
          </TransitionGroup>
        </div>
      </div>
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
      loading: true,
      error: null,
      viewMode: 'grid',
      sortOption: 'date-desc',
      styles: [
        'Style Moderne Minimaliste',
        'Style Rustique',
        'Style Scandinave',
        'Style Industriel',
        'Style Traditionnel',
        'Style Art Déco',
        'Style Contemporain',
        'Style High-Tech',
        'Style Bohème',
        'Style Champêtre'
      ],
      styleMapping: {
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
    },
    sortedGenerations() {
      return [...this.filteredGenerations].sort((a, b) => {
        switch (this.sortOption) {
          case 'date-asc':
            return new Date(a.creation_date) - new Date(b.creation_date)
          case 'date-desc':
            return new Date(b.creation_date) - new Date(a.creation_date)
          case 'duration':
            return a.processing_duration - b.processing_duration
          default:
            return 0
        }
      })
    }
  },
  methods: {
    async fetchGenerations() {
      try {
        this.loading = true
        this.error = null
        const response = await axios.get('http://localhost:8081/stockage/prompts')
        this.pastgenerations = (response.data.message || response.data).reverse()
      } catch (error) {
        this.error = 'Erreur lors du chargement des transformations'
        console.error('Error fetching data:', error)
      } finally {
        this.loading = false
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

<style scoped>
/* Animations de transition pour la liste */
.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(30px);
}

.list-leave-active {
  position: absolute;
}

/* Animation du loader */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Style pour le scroll */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background: #9CA3AF;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #4B5563;
}
</style>
