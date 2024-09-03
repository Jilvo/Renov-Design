<template>
  <Header />
  <LoginForm />
</template>
<script>
import Header from '../components/Header/Header.vue'
import LoginForm from '../components/Login/LoginForm.vue'
export default {
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Header,
    LoginForm
  }
}
</script>
