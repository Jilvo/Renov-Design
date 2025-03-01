<template>
  <Header />
  <!-- <div>Redesignez votre maison</div> -->
  <body class="font-body">
    <!-- home section -->
    <section class="bg-white mb-20">
      <div class="container max-w-screen-xl mx-auto px-4">
        <div class="flex items-center justify-center">
          <div class="mt-28 text-center">
            <h1
              class="font-semibold text-4xl md:text-6xl lg:text-7xl text-gray-900 leading-normal mb-6"
            >
              Transformez votre intérieur<br />
              grâce à l'IA
            </h1>

            <p class="font-normal text-xl text-gray-400 leading-relaxed mb-12">
              Visualisez instantanément le nouveau design de vos pièces<br />
              avec notre technologie d'intelligence artificielle.
            </p>

            <button
              class="px-6 py-4 bg-green-700 text-white font-semibold text-lg rounded-xl hover:bg-green-900 transition ease-in-out duration-500"
            >
              Transformer ma pièce
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- feature section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4">
        <div class="flex flex-col justify-center">
          <div class="">
            <h1
              class="font-semibold text-gray-900 text-xl md:text-4xl text-center leading-normal mb-6"
            >
              Une transformation simple<br />
              en quelques clics
            </h1>

            <p class="font-normal text-gray-400 text-md md:text-xl text-center mb-16">
              Notre IA analyse votre photo et la transforme<br />
              selon le style de votre choix.
            </p>

            <div class="flex flex-col md:flex-row justify-center space-x-4 mb-20">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="check-circle" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Résultat réaliste</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  Notre IA génère des images ultra-réalistes<br />
                  fidèles à votre intérieur.
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row justify-center space-x-4 mb-20">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="lock" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Transformation rapide</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  Obtenez le résultat en quelques secondes,<br />
                  sans attente ni délai.
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row justify-center space-x-4">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="credit-card" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Styles variés</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  Moderne, Scandinave, Industriel, Classique...<br />
                  Choisissez parmi nos nombreux styles.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- testimoni section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4">
        <p class="font-normal text-gray-400 text-lg md:text-xl text-center uppercase mb-6">
          Témoignages
        </p>

        <h1
          class="font-semibold text-gray-900 text-2xl md:text-4xl text-center leading-normal mb-14"
        >
          Ce que nos utilisateurs<br />
          pensent de leurs transformations
        </h1>

        <div
          class="flex flex-col md:flex-row md:items-center justify-center md:space-x-8 lg:space-x-12 mb-10 md:mb-20"
        >
          <div class="bg-gray-100 rounded-lg mb-10 md:mb-0 p-8">
            <div class="flex items-center gap-5 mb-8">
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
            </div>

            <p class="font-normal text-sm lg:text-md text-gray-400 mb-8">
              Je suis impressionné par la qualité des transformations. <br />
              L'IA a parfaitement compris mon style et a transformé mon salon<br />
              exactement comme je l'imaginais. Le résultat est bluffant<br />
              de réalisme. Je recommande vivement !
            </p>

            <h3 class="font-semibold text-gray-900 text-xl md:text-2xl lg:text-3xl">
              Marie Dupont
            </h3>
          </div>

          <div class="bg-gray-100 rounded-lg p-8">
            <div class="flex items-center gap-5 mb-8">
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
            </div>

            <p class="font-normal text-sm lg:text-md text-gray-400 mb-8">
              Un outil révolutionnaire pour visualiser les changements<br />
              avant de se lancer dans les travaux. J'ai pu tester différents<br />
              styles pour ma chambre et choisir celui qui me correspondait<br />
              le mieux. Le rendu est vraiment professionnel !
            </p>

            <h3 class="font-semibold text-gray-900 text-xl md:text-2xl lg:text-3xl">
              Thomas Martin
            </h3>
          </div>
        </div>
      </div>
    </section>

    <!-- contact section -->
    <section class="bg-white py-10 md:py-16" id="contact">
      <div class="container max-w-screen-xl mx-auto px-4">
        <div
          class="bg-green-800 flex flex-col lg:flex-row items-center justify-evenly py-14 rounded-3xl"
        >
          <div class="text-center lg:text-left mb-10 lg:mb-0">
            <h1
              class="font-semibold text-white text-4xl md:text-5xl lg:text-7xl leading-normal mb-4"
            >
              Des questions ?
            </h1>

            <p class="font-normal text-white text-md md:text-xl">
              Notre équipe est là pour vous accompagner<br />
              dans votre projet de transformation.
            </p>
          </div>

          <div class="bg-white px-6 py-3 rounded-3xl">
            <div class="py-3">
              <h3 class="font-semibold text-gray-900 text-3xl">Contactez-nous</h3>
            </div>

            <div class="py-3">
              <input
                type="text"
                placeholder="Nom complet"
                class="px-4 py-4 w-96 bg-gray-100 placeholder-gray-400 rounded-xl outline-none"
              />
            </div>

            <div class="py-3">
              <input
                type="text"
                placeholder="Email"
                class="px-4 py-4 w-96 bg-gray-100 placeholder-gray-400 rounded-xl outline-none"
              />
            </div>

            <div class="py-3">
              <input
                type="text"
                placeholder="Message"
                class="px-4 py-10 w-96 bg-gray-100 placeholder-gray-400 rounded-xl outline-none"
              />
            </div>

            <div class="py-3">
              <button
                class="w-full py-4 font-semibold text-lg text-white bg-green-700 rounded-xl hover:bg-green-900 transition ease-in-out duration-500"
              >
                Envoyer
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
import Header from '../components/Header/Header.vue'

export default {
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Header
  }
}
</script>