<template>
    <div class="container">
    <div class = "col-md-12 justify-content-center h-100">
        <div class = "row">
            <div class= "col-md-2"></div>
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">
                        <h3>Posteaza un anunt</h3>
                    </div>
                    <div class="card-body">
                        <div class="alert alert-danger" role="alert" v-if = "this.errors">
                            <i class = "fas fa-ban-o"></i> Ne pare rau, anuntul tau nu a putut fi postat.
                        </div>
                        <div class="form-group">
                            <label>Categorie anunt</label>
                            <select class="form-control" v-model="input.category">
                                <option value = "0" selected>Mancare</option>
                                <option value = "1">Servicii</option>
                                <option value = "2">Bunuri</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Titlu anunt</label>
                            <input type="text" v-model="input.title" class="form-control" placeholder="...">
                        </div>
                        <div class="form-group">
                            <label>Descriere</label>
                            <textarea v-model="input.description" class="form-control" placeholder="..."></textarea>
                        </div>
                        <div class="form-group">
                            <label>Localitate</label>
                            <select class = "form-control" data-live-search="true" v-model="input.city">
                                <option v-for="oras in this.orase" :id="oras.nume">{{ oras.nume }}</option>
                            </select>
                        </div>
                        <br>
                        <center><input type="submit" v-on:click="add()" value="Adauga anunt" class="btn btn btn-outline-primary"></center>
                    </div>    
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'Login',
        data() 
        {
            return {
                input: 
                {
                    category: "",
                    title: "",
                    description: "",
                    city: "",
                },
                errors: false,
                orase: []
            }
        },
        mounted() 
        {
            if(!this.$cookie.get('loggedIn')) 
            {
                this.$router.push("/login");
                return;
            }


            let _this = this;
            axios.get("https://raw.githubusercontent.com/catalin87/baza-de-date-localitati-romania/master/date/localitati.json").then(function(response) {
                _this.orase = response.data;
            });
        },
        methods: 
        {
            add() 
            {
                if(this.input.category != "" && this.input.title != "" && this.input.description != "" && this.input.city != "")
                {   
                    this.errors = false;   
                    let _this = this;

                    axios.post("http://vps1.thecodeleones.club/adregister", { category: this.input.category, title: this.input.title, description: this.input.description, location: this.input.city, userid: _this.$cookie.get('loggedIn') }).then(function(response)
                    {
                        let apiResponse = response.data;

                        if(apiResponse.status !== "True") 
                        {
                            _this.errors = true;
                        }
                        else 
                        {
                            window.location = "/anunt/"+apiResponse.id;
                        }
                    });
                }
            }
        }
    }
</script>