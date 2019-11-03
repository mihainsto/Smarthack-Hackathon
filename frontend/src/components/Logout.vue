<template>
</template>

<script>
    export default 
    {
        mounted() 
        {
            this.$cookie.delete('loggedIn');
            this.$cookie.delete('userName');
            window.location = "/";
            window.location = "/";
        }
    }
</script>