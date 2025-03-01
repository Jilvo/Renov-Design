<template>
  <section class="min-h-screen bg-gradient-to-br from-green-50 to-green-100 dark:from-gray-900 dark:to-gray-800">
    <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto min-h-screen lg:py-0">
      <div
        class="w-full bg-white rounded-2xl shadow-lg transform hover:scale-[1.02] transition-all duration-300 dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700"
      >
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-2xl font-bold leading-tight tracking-tight bg-gradient-to-r from-green-600 to-green-800 bg-clip-text text-transparent md:text-3xl"
          >
            Connexion
          </h1>
          <form class="space-y-4 md:space-y-6" @submit.prevent="submitForm">
            <div class="group">
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white transition-colors duration-200"
                >Votre email</label
              >
              <input
                type="email"
                v-model="form.email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-green-500 block w-full p-3 transform transition-all duration-200 ease-in-out hover:shadow-md dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
                placeholder="nom@exemple.com"
                required
              />
            </div>
            <div class="group">
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white transition-colors duration-200"
                >Mot de passe</label
              >
              <input
                type="password"
                v-model="form.password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-green-500 block w-full p-3 transform transition-all duration-200 ease-in-out hover:shadow-md dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
                required
              />
            </div>
            <div class="flex items-center justify-between">
              <div class="flex items-start">
                <div class="flex items-center h-5">
                  <input
                    id="remember"
                    aria-describedby="remember"
                    type="checkbox"
                    v-model="form.remember"
                    class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-green-300 cursor-pointer transition-colors duration-200 dark:bg-gray-700 dark:border-gray-600"
                  />
                </div>
                <div class="ml-3 text-sm">
                  <label for="remember" class="text-gray-500 dark:text-gray-300">Se souvenir de moi</label>
                </div>
              </div>
              <a
                href="#"
                class="text-sm font-medium text-green-600 hover:text-green-800 transition-colors duration-200 dark:text-green-400 dark:hover:text-green-300"
                >Mot de passe oublié ?</a
              >
            </div>
            <button
              type="submit"
              class="w-full text-white bg-gradient-to-r from-green-600 to-green-800 hover:from-green-700 hover:to-green-900 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-xl text-sm px-5 py-3 text-center transform transition-all duration-200 ease-in-out hover:scale-[1.02] hover:shadow-lg dark:focus:ring-green-800"
            >
              Se connecter
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Pas encore de compte ?
              <a
                href="/sign-up"
                class="font-medium text-green-600 hover:text-green-800 transition-colors duration-200 dark:text-green-400 dark:hover:text-green-300"
                >S'inscrire</a
              >
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        password: '',
        remember: false
      }
    }
  },
  methods: {
    submitForm() {
      console.log('Formulaire soumis:', this.form)
      // Ici vous gérerez la soumission du formulaire vers votre backend
    }
  }
}
</script>

<style scoped>
.group:focus-within label {
  color: #059669;
}

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

input:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(5, 150, 105, 0.2);
}

button:active {
  transform: scale(0.98);
}
</style>
