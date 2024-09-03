<template>
  <Header />
  <SignUp />
</template>
<script>
import Header from '../components/Header/Header.vue'
import SignUp from '../components/Signup/SignupForm.vue'
export default {
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Header,
    SignUp
  }
}
</script>
