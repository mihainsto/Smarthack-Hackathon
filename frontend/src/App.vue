<template>
  <div id="app">
    <div id = "header">
      <my-header></my-header>
    </div>
    <router-view/>
  </div>
</template>

<script>
  import Header from './components/Header.vue'

  export default 
  {
    name: 'App',
    components:
    {
      'my-header': Header
    }
  }
</script>
