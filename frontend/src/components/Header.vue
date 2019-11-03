<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <router-link to = "/" class = "navbar-brand">MOKA</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                    <router-link to = "/" class = "nav-item nav-link">Acasa</router-link>
                    <router-link to = "/anunturi" class = "nav-item nav-link">Am nevoie</router-link>
                    <router-link to = "/ofer" class = "nav-item nav-link" v-if="this.$cookie.get('loggedIn')">Ofer</router-link>
                </div> 
            </div>
            <div class = "float-right">    
                <router-link class="btn btn-outline-primary" to="/login" v-if = "!this.$cookie.get('loggedIn')"><i class="fas fa-sign-in-alt"></i> Autentificare</router-link>
                <span v-if = "this.$cookie.get('loggedIn')">
                    <router-link class="btn btn-outline-primary" to="/alerte"><i class="fas fa-exclamation-triangle"></i> Adauga alerte</router-link>
                    <router-link class="btn btn-outline-primary" to = "logout">{{ this.$cookie.get('userName') }} <i class = "fas fa-sign-out-alt"></i></router-link>
                </span>  
            </div>   
        </nav>
        <br>
    </div>    
</template>
