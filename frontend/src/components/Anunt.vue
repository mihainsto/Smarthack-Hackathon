<template>
    <div class = "col-md-12" v-if="user_data !== null">
        <div class = "row">
            <div class = "col-md-8">
                <div class="alert alert-danger" role="alert" v-if = "this.active == 0">
                    <i class="fas fa-exclamation"></i> Acest anunt a fost marcat drept inactiv de catre utilizatorul care l-a postat.
                </div>
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title" style = "text-transform:uppercase;">{{ title }}</h3>
                        <p class="card-text"><div class = "float-left"><i class="fas fa-location-arrow"></i> {{ location }}</div> <div class = "float-right"><i class="far fa-clock"></i> {{ time }}</div></p>
                        <br>
                        <hr>
                        {{ description }}            
                    </div>
                </div>
            </div>
            <div class = "col-md-2">
                Postat de catre utilizatorul {{ user_data.username }}
                <a v-bind:href = "mailto+user_data.email"><button type="button" class="btn btn-primary"><i class="fas fa-inbox"></i> Contacteaza utilizatorul</button></a><br>
                <button type="button" class="btn btn-primary" v-on:click="showNumber()" style = "margin-top:5px;" v-html = "number"></button>
                
                <div v-if = "(this.user_data.id == this.$cookie.get('loggedIn') && this.active == 1)">
                    <hr>
                    <div class="card">
                        <div class="card-body">
                            <center>
                                <div>
                                    <button type="button" class="btn btn-success" v-on:click="toggleStatus()">Marcheaza drept inactiv</button>
                                </div>
                            </center>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>    
</template>

<script>
    import axios from "axios";

    export default 
    {
        data() 
        {
            return {
                title: "",
                location: "",
                time: "",
                description: "",
                user_data: null,
                active: null,
                mailto: "mailto:",
                number: "<i class='fas fa-phone'></i> ********** <small>Arata numar</small>"
            };
        },
        mounted() {
            let _this = this;
            axios.post("http://vps1.thecodeleones.club/addetails", { id: this.$route.params.id }).then(function(response) {
                _this.title = response.data.title;
                _this.location = response.data.location;
                _this.time = response.data.post_time;
                _this.description = response.data.description;
                _this.active = response.data.active;

                axios.post("http://vps1.thecodeleones.club/userdetails", {id: response.data.user_id}).then(function(resp) {
                    _this.user_data = resp.data;
                    _this.user_data.id = response.data.user_id;
                });
            });
        },
        methods: {
            showNumber: function() {
                this.number = `<i class="fas fa-phone"></i> ${this.user_data.phone_number}`;
            },
            toggleStatus: function() {
                if(this.user_data.id != this.$cookie.get('loggedIn')) return;

                let _this = this;

                axios.post("http://vps1.thecodeleones.club/changeadstatus", {id: this.$route.params.id, status: 0}).then(function(response) {
                    if(response.data.status == "True") _this.active = false;
                });
            }
        }
    }
</script>