<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-white border-gray-200 dark:bg-gray-900">
    <div class="max-w-screen-2xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
        <img :src="navbarlogo" alt="Logo" class="h-8" />
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">
          Renov-Design
        </span>
      </a>
      <div class="hidden w-full md:block md:w-auto ml-auto" id="navbar-default">
        <ul
          class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
        >
          <li>
            <a href="/history" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 dark:text-white">History</a>
          </li>
          <li>
            <a href="/past-generations" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 dark:text-white">Few Generations</a>
          </li>
          <li>
            <a href="/generate" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 dark:text-white">Generate</a>
          </li>
          <li v-if="!username">
            <a href="/login" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 dark:text-white">Login</a>
          </li>
          <li v-if="username">
            <span class="block py-2 px-3 text-gray-900 dark:text-white">Bienvenue, {{ username }}</span>
          </li>
          <li>
            <a href="/#contact" class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 dark:text-white">Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'
// import { useJwt } from '@vueuse/integrations/useJwt'
// import { defineComponent } from 'vue'
import navbarlogo from '@/assets/images/navbar-logo.png'

const username = ref('')

onMounted(() => {
  const token = localStorage.getItem('token')
  if (token) {
    try {
      console.log("test")
      console.log(token)
      // const decoded = jwt_decode(token)
      // const { header, payload } = useJwt(token)
      // console.log(header)
      // console.log(payload)
      // Vérifie si le token a expiré
      // const currentTime = Math.floor(Date.now() / 1000) // Heure actuelle en secondes
      // if (decoded.exp && decoded.exp > currentTime) {
      //   username.value = decoded.username
      // } else {
      //   console.warn('Token has expired')
      //   localStorage.removeItem('token') // Supprime le token expiré
      // }
    } catch (error) {
      console.error('Invalid token', error)
      localStorage.removeItem('token') // Supprime le token invalide
    }
  }
})
</script>
