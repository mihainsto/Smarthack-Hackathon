<template>
    <div>
        <div class = "container" v-if = "this.orase != null">
            <div class = "col-md-12">
                <div class = "form-row">
                    <div class="input-group col-md-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class="fas fa-search"></i></span>
                        </div>
                        <input type="text" class="form-control" v-model="input.keyword" placeholder = "Text.."></input>
                    </div>

                    <div class="input-group col-md-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class="fas fa-list"></i></span>
                        </div>
                        <select class="form-control" v-model="input.category">
                            <option value = "0">Mancare</option>
                            <option value = "1">Servicii</option>
                            <option value = "2">Bunuri</option>
                        </select>
                    </div>

                    <div class="input-group col-md-3">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class="fas fa-map-marker-alt"></i></span>
                        </div>
                        <select class="form-control" v-model="input.location">
                            <option value = "%%">Oriunde</option>
                            <option v-for="oras in this.orase" :id="oras.nume">{{ oras.nume }}</option>
                        </select>
                    </div>

                    <div class="input-group col-md-3 justify-content-center">
                        <button type="button" class="btn btn-primary btn-sm" v-on:click="searchAds();"><i class="fas fa-search"></i> Search</button>
                    </div>
                </div>
            </div>
        </div>
        <hr>
        <div v-if = "results != []">
            <div v-for="ad in results">
                <div class="card">
                    <div class="card-body">
                        <h3 class="card-title" style = "text-transform:uppercase;"><a href = "#" v-on:click = "viewAd(ad.id)">{{ ad.title }}</a></h3>
                        <p class="card-text"><div class = "float-left"><i class="fas fa-location-arrow"></i> {{ ad.location }}</div> <div class = "float-right"><i class="far fa-clock"></i> {{ ad.post_time }}</div></p>
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
                orase: null,
                anunturi: [],
                input: { keyword: "", category: "0", location: "%%"},
                results: [],
            }
        },
        mounted() 
        {
            let _this = this;
            axios.get("https://raw.githubusercontent.com/catalin87/baza-de-date-localitati-romania/master/date/localitati.json").then(function(response) {
                _this.orase = response.data;
            });
        },
        methods: {
            searchAds: function() 
            {
                let vue = this;
                
                vue.results = [];

                axios.post("http://vps1.thecodeleones.club/addfiltercategorylocation", {location: this.input.location, category: this.input.category}).then(function(result) {
                    let apiResult = result.data;

                    console.log(apiResult);

                    apiResult.forEach(function(ad) {
                        if(!ad.status) return;
                        if(!ad.title.includes(vue.input.keyword) && vue.input.keyword !== "") return;

                        console.log(ad);

                        vue.results.push(ad);
                    })
                });
            },
            viewAd: function(id) 
            {
                this.$router.push('/anunt/'+id);
            }
        }
    }
</script>