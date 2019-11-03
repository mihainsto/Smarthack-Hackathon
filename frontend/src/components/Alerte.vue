<template>
    <div class = "container">
        <div class = "row">
            <div class = "col-md-3"></div>
            <div class = "col-md-6">
                <div class="card">
                    <div class="card-header">
                        <h3>Alertele tale</h3>
                    </div>

                    <div class = "card-body">
                        <div class="table-responsive">
                            <table class = "table" v-if="alerts != []">
                                <tr>
                                    <td>Stergere</td>
                                    <td>Categorie</td>
                                    <td>Cuvinte cheie</td>
                                </tr>
                                <tr v-for = "alerta in this.alerts">
                                    <td><button class = "btn btn-sm btn-danger" v-on:click = "deleteAlert( alerta.id, alerta )"><i class="fas fa-trash"></i></button></td>
                                    <td>{{ alerta.category == 0 ? "Mancare" : (alerta.category == 1 ? "Servicii" : "Bunuri") }}</td>
                                    <td>{{ alerta.keyword }}</td>
                                </tr>
                            </table>
                        </div>    
                    </div>

                    <div class = "card-body">
                        <button class="btn btn-primary btn-sm" type="button" data-toggle="collapse" data-target="#adaugaAlerta" aria-expanded="false" aria-controls="adaugaAlerta" style = "width: 80%; margin-left: 10%;">Adauga o noua alerta</button>                  

                        <div class="collapse multi-collapse" id="adaugaAlerta">
                            <br>
                            <div class="card card-body">
                                <div class="form-group">
                                    <label>Cuvinte cheie</label>
                                    <input type="text" class="form-control" v-model="input.preference" placeholder="masina de spalat">
                                </div>

                                <div class = "form-group">
                                    <label>Categorie</label>
                                    <select class="form-control" v-model="input.category">
                                        <option value = "0" selected>Mancare</option>
                                        <option value = "1">Servicii</option>
                                        <option value = "2">Bunuri</option>
                                    </select>                                            
                                </div>
                                
                                <button class = "btn btn-primary btn-success btn-sm" v-on:click="addAlert();">Adauga alerta</button>
                                <button class = "btn btn-primary btn-danger btn-sm" style = "margin-top: 2px;" data-toggle="collapse" data-target="#adaugaAlerta">Anulare</button>
                            </div>
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
        data() {
           return {
               alerts: [],
               input: { preference: "", category: ""},
           }     
        }, 
        mounted() {
            let vue = this;

            vue.alerts = [];

            axios.post("http://vps1.thecodeleones.club/getpreferences", { user_id: vue.$cookie.get('loggedIn') }).then(function(response) {
                vue.alerts = response.data;
            });
        }, 
        methods: {
            deleteAlert: function(id, alerta) {

                let vue = this;

               axios.post("http://vps1.thecodeleones.club//removepreference", { id: id }).then(function(response) {
                   let apiResponse = response.data;

                   if(apiResponse.status == "True") 
                   {
                      vue.alerts.splice(vue.alerts.indexOf(alerta), 1);  
                   }
               });
            },
            addAlert: function() 
            {
                if(this.input.preference != "" && this.input.category != "") 
                {
                    let vue = this;

                    axios.post("http://vps1.thecodeleones.club/addpreferece", { user_id: 1, category : this.input.category, preference : this.input.preference }).then(function(result) {
                        let apiResponse = result.data;

                        if(apiResponse.status == "True") 
                        {
                            vue.alerts.push({ id: apiResponse.id, keyword: vue.input.preference, category: vue.input.category });
                        }
                    });  
                }
            }
        }
    }
</script>