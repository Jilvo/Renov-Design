<template>
  <Header />
  <div>Redesignez votre maison</div>
  <body class="font-body">
    <!-- home section -->
    <section class="bg-white mb-20 md:mb-52 xl:mb-72">
      <div class="container max-w-screen-xl mx-auto px-4">
        <nav
          class="flex-wrap lg:flex items-center py-14 xl:relative z-10"
          x-data="{navbarOpen:false}"
        >
          <div class="flex items-center justify-between mb-10 lg:mb-0">
            <img :src="navbarlogo" alt="Logo img" class="w-52 md:w-80 lg:w-full" />

            <button
              class="lg:hidden w-10 h-10 ml-auto flex items-center justify-center text-green-700 border border-green-700 rounded-md"
              @click="navbarOpen = !navbarOpen"
            >
              <i data-feather="menu"></i>
            </button>
          </div>

          <ul
            class="lg:flex flex-col lg:flex-row lg:items-center lg:mx-auto lg:space-x-8 xl:space-x-16"
            :class="{ hidden: !navbarOpen, flex: navbarOpen }"
          >
            <li
              class="font-semibold text-gray-900 text-lg hover:text-gray-400 transition ease-in-out duration-300 mb-5 lg:mb-0"
            >
              <a href="#">Landing</a>
            </li>

            <li
              class="font-semibold text-gray-900 text-lg hover:text-gray-400 transition ease-in-out duration-300 mb-5 lg:mb-0"
            >
              <a href="#">Pages</a>
            </li>

            <li
              class="font-semibold text-gray-900 text-lg hover:text-gray-400 transition ease-in-out duration-300 mb-5 lg:mb-0"
            >
              <a href="#">Contact</a>
            </li>

            <li
              class="font-semibold text-gray-900 text-lg hover:text-gray-400 transition ease-in-out duration-300 mb-5 lg:mb-0"
            >
              <a href="#">About</a>
            </li>
          </ul>

          <button
            class="px-5 py-3 lg:block border-2 border-green-700 rounded-lg font-semibold text-green-700 text-lg hover:bg-green-700 hover:text-white transition ease-linear duration-500"
            :class="{ hidden: !navbarOpen, flex: navbarOpen }"
          >
            Request quote
          </button>
        </nav>

        <div class="flex items-center justify-center xl:justify-start">
          <div class="mt-28 text-center xl:text-left">
            <h1
              class="font-semibold text-4xl md:text-6xl lg:text-7xl text-gray-900 leading-normal mb-6"
            >
              Get your dream <br />
              house now
            </h1>

            <p class="font-normal text-xl text-gray-400 leading-relaxed mb-12">
              Having a sweet home is everyone's dream. Have you <br />
              owned your dream house?
            </p>

            <button
              class="px-6 py-4 bg-green-700 text-white font-semibold text-lg rounded-xl hover:bg-green-900 transition ease-in-out duration-500"
            >
              Contact us
            </button>
          </div>

          <div class="hidden xl:block xl:absolute z-0 top-0 right-0">
            <img :src="homeimg" alt="Home img" />
          </div>
        </div>
      </div>
      <!-- container.// -->
    </section>
    <!-- home section //nd -->

    <!-- feature section -->
    <section class="bg-white py-10 md:py-16 xl:relative">
      <div class="container max-w-screen-xl mx-auto px-4">
        <div class="flex flex-col xl:flex-row justify-end">
          <div class="hidden xl:block xl:absolute left-0 bottom-0 w-full">
            <img :src="featureimg" alt="Feature img" />
          </div>

          <div class="">
            <h1
              class="font-semibold text-gray-900 text-xl md:text-4xl text-center leading-normal mb-6"
            >
              Choice of various types of <br />
              house
            </h1>

            <p class="font-normal text-gray-400 text-md md:text-xl text-center mb-16">
              We provide a wide of selection of home types for you and your <br />
              family and are free to choose a home model
            </p>

            <div class="flex flex-col md:flex-row justify-center xl:justify-start space-x-4 mb-20">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="check-circle" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Best Home Guarantee</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  We guarantees the quality of your home you bought <br />
                  from D’house
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row justify-center xl:justify-start space-x-4 mb-20">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="lock" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Safe Transaction</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  Your transactions will always be kept confidential <br />
                  and will get discounted
                </p>
              </div>
            </div>

            <div class="flex flex-col md:flex-row justify-center xl:justify-start space-x-4">
              <div
                class="px-8 h-20 mx-auto md:mx-0 bg-gray-200 rounded-lg flex items-center justify-center mb-5 md:mb-0"
              >
                <i data-feather="credit-card" class="text-green-900"></i>
              </div>

              <div class="text-center md:text-left">
                <h4 class="font-semibold text-gray-900 text-2xl mb-2">Low and Cost Home Taxes</h4>
                <p class="font-normal text-gray-400 text-xl leading-relaxed">
                  By buying a house from D’house, you will get a tax <br />
                  discount
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- container.// -->
    </section>
    <!-- feature section //end -->

    <!-- gallery section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4">
        <h1 class="font-semibold text-gray-900 text-4xl text-center mb-10">Our Gallery</h1>

        <div class="hidden md:block flex items-center text-center space-x-10 lg:space-x-20 mb-12">
          <a
            href="#"
            class="px-6 py-2 bg-green-800 text-white font-semibold text-xl rounded-lg hover:bg-green-600 transition ease-in-out duration-500"
            >All</a
          >
          <a
            href="#"
            class="px-6 py-2 text-gray-900 font-normal text-xl rounded-lg hover:bg-gray-200 hover:text-gray-400 transition ease-in-out duration-500"
            >Exterior</a
          >
          <a
            href="#"
            class="px-6 py-2 text-gray-900 font-normal text-xl rounded-lg hover:bg-gray-200 hover:text-gray-400 transition ease-in-out duration-500"
            >Interior</a
          >
          <a
            href="#"
            class="px-6 py-2 text-gray-900 font-normal text-xl rounded-lg hover:bg-gray-200 hover:text-gray-400 transition ease-in-out duration-500"
            >Building</a
          >
        </div>

        <div class="flex space-x-4 md:space-x-6 lg:space-x-8">
          <div>
            <img
              :src="gallery1"
              alt="image"
              class="mb-4 md:mb-6 lg:mb-8 hover:opacity-75 transition ease-in-out duration-500"
            />
            <img
              :src="gallery4"
              alt="image"
              class="hover:opacity-75 transition ease-in-out duration-500"
            />
          </div>

          <div>
            <img
              :src="gallery2"
              alt="image"
              class="mb-4 md:mb-6 lg:mb-8 hover:opacity-75 transition ease-in-out duration-500"
            />
            <img
              :src="gallery5"
              alt="image"
              class="mb-3 md:mb-6 lg:mb-8 hover:opacity-75 transition ease-in-out duration-500"
            />
            <img
              :src="gallery6"
              alt="image"
              class="hover:opacity-75 transition ease-in-out duration-500"
            />
          </div>

          <div>
            <img
              :src="gallery3"
              alt="image"
              class="mb-4 md:mb-6 lg:mb-8 hover:opacity-75 transition ease-in-out duration-500"
            />
            <img
              :src="gallery7"
              alt="image"
              class="hover:opacity-75 transition ease-in-out duration-500"
            />
          </div>
        </div>
      </div>
      <!-- container.// -->
    </section>
    <!-- gallery section //end -->

    <!-- testimoni section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4 xl:relative">
        <p class="font-normal text-gray-400 text-lg md:text-xl text-center uppercase mb-6">
          Testimonial
        </p>

        <h1
          class="font-semibold text-gray-900 text-2xl md:text-4xl text-center leading-normal mb-14"
        >
          What People Say <br />
          About D’house
        </h1>

        <div class="hidden xl:block xl:absolute top-0">
          <img :src="testimoni1" alt="Image" />
        </div>

        <div class="hidden xl:block xl:absolute top-32">
          <img :src="testimoni2" alt="Image" />
        </div>

        <div
          class="flex flex-col md:flex-row md:items-center justify-center md:space-x-8 lg:space-x-12 mb-10 md:mb-20"
        >
          <div class="bg-gray-100 rounded-lg mb-10 md:mb-0">
            <img :src="testimoni3" alt="Image" class="mx-8 my-8" />

            <div class="flex items-center gap-5 mx-8">
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
            </div>

            <p class="font-normal text-sm lg:text-md text-gray-400 mx-8 my-8">
              I recommend anyone to buy house on <br />
              D’house. I received great customer service <br />
              from the specialists who helped me.
            </p>

            <h3 class="font-semibold text-gray-900 text-xl md:text-2xl lg:text-3xl mx-8 mb-8">
              Brooklyn Simmons
            </h3>
          </div>

          <div class="bg-gray-100 rounded-lg">
            <img :src="testimoni4" alt="Image" class="mx-8 my-8" />

            <div class="flex items-center gap-5 mx-8">
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
              <i data-feather="star" class="text-yellow-500"></i>
            </div>

            <p class="font-normal text-sm lg:text-md text-gray-400 mx-8 my-8">
              D’house is the best property agent in the <br />
              world. I received great customer service <br />
              from the D’house agent
            </p>

            <h3 class="font-semibold text-gray-900 text-xl md:text-2xl lg:text-3xl mx-8 mb-8">
              Ralph Edwards
            </h3>
          </div>
        </div>
      </div>
      <!-- container.// -->
    </section>
    <!-- testimoni section //end -->

    <!-- book section -->
    <section class="bg-white py-10 md:py-16">
      <div class="container max-w-screen-xl mx-auto px-4 xl:relative">
        <div
          class="bg-green-800 flex flex-col lg:flex-row items-center justify-evenly py-14 rounded-3xl"
        >
          <div class="text-center lg:text-left mb-10 lg:mb-0">
            <h1
              class="font-semibold text-white text-4xl md:text-5xl lg:text-7xl leading-normal mb-4"
            >
              Talk to us <br />
              to discuss
            </h1>

            <p class="font-normal text-white text-md md:text-xl">
              Need more time to discuss? Won’t worry, we are <br />
              ready to help you. You can fill in the column on the <br />
              right to book a meeting with us. Totally free.
            </p>
          </div>

          <div class="hidden xl:block xl:absolute right-0">
            <img :src="book" alt="Image" />
          </div>

          <div class="hidden md:block bg-white xl:relative px-6 py-3 rounded-3xl">
            <div class="py-3">
              <h3 class="font-semibold text-gray-900 text-3xl">Book a meeting</h3>
            </div>

            <div class="py-3">
              <input
                type="text"
                placeholder="Full Name"
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

            <div class="py-3 relative">
              <input
                type="text"
                placeholder="Date"
                class="px-4 py-4 w-96 bg-gray-100 font-normal text-lg placeholder-gray-400 rounded-xl outline-none"
              />

              <div class="absolute inset-y-0 left-80 ml-6 flex items-center text-xl text-gray-600">
                <i data-feather="calendar"></i>
              </div>
            </div>

            <div class="py-3 relative">
              <input
                type="text"
                placeholder="Virtual Meeting"
                class="px-4 py-4 w-96 bg-gray-100 placeholder-gray-400 rounded-xl outline-none"
              />

              <div class="absolute inset-y-0 left-80 ml-6 flex items-center text-xl text-gray-600">
                <i data-feather="chevron-down"></i>
              </div>
            </div>

            <div class="py-3">
              <button
                class="w-full py-4 font-semibold text-lg text-white bg-green-700 rounded-xl hover:bg-green-900 transition ease-in-out duration-500"
              >
                Booking
              </button>
            </div>
          </div>
        </div>
      </div>
      <!-- container.// -->
    </section>
    <!-- book section //end -->

    <!-- home section //nd -->
  </body>
</template>

<script>
import Header from '../components/Header/Header.vue'
import book from '@/assets/images/book.png'
import featureimg from '@/assets/images/feature-img.png'
import footerlogo from '@/assets/images/footer-logo.png'
import gallery1 from '@/assets/images/gallery-1.png'
import gallery2 from '@/assets/images/gallery-2.png'
import gallery3 from '@/assets/images/gallery-3.png'
import gallery4 from '@/assets/images/gallery-4.png'
import gallery5 from '@/assets/images/gallery-5.png'
import gallery6 from '@/assets/images/gallery-6.png'
import gallery7 from '@/assets/images/gallery-7.png'
import homeimg from '@/assets/images/home-img.png'
import navbarlogo from '@/assets/images/navbar-logo.png'
import testimoni1 from '@/assets/images/testimoni-1.png'
import testimoni2 from '@/assets/images/testimoni-2.png'
import testimoni3 from '@/assets/images/testimoni-3.png'
import testimoni4 from '@/assets/images/testimoni-4.png'

export default {
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Header
  },
  data() {
    return {
      book: book,
      featureimg: featureimg,
      footerlogo: footerlogo,
      gallery1: gallery1,
      gallery2: gallery2,
      gallery3: gallery3,
      gallery4: gallery4,
      gallery5: gallery5,
      gallery6: gallery6,
      gallery7: gallery7,
      homeimg: homeimg,
      navbarlogo: navbarlogo,
      testimoni1: testimoni1,
      testimoni2: testimoni2,
      testimoni3: testimoni3,
      testimoni4: testimoni4
    }
  }
}
</script>
