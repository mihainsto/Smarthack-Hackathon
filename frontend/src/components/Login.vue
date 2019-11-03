<template>
    <div class="container">
	<div class="d-flex justify-content-center h-100">
		<div class="card">
			<div class="card-header">
				<h3>Autentificare</h3>
			</div>
			<div class="card-body">
                <div class="alert alert-danger" role="alert" v-if = "this.errors">
                    <i class = "fas fa-ban-o"></i> Date de autentificare invalide
                </div>
                <div class="input-group form-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text"><i class="fas fa-user"></i></span>
                    </div>
                    <input type="text" v-model="input.username" class="form-control" placeholder="Nume de utilizator">
                </div>
                <div class="input-group form-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text"><i class="fas fa-key"></i></span>
                    </div>
                    <input type="password" v-model="input.password" class="form-control" placeholder="Parola">
                </div>
                <div class="form-group">
                    <input type="submit" v-on:click="login()" value="Autentificare" class="btn float-right btn btn-outline-primary">
                </div>
			</div>
			<div class="card-footer">
				<div class="d-flex justify-content-center links">
					<router-link class="" to="/register">Nu ai cont? Inregistreaza-te</a></router-link>
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
                    username: "",
                    password: "",
                },
                errors: false
            }
        },
        methods: 
        {
            login() 
            {
                if(this.input.username != "" && this.input.password != "")
                {   
                    this.errors = false;   
                    let _this = this;

                    axios.post("http://vps1.thecodeleones.club/auth", { username: this.input.username, password: this.input.password }).then(function(response)
                    {
                        let apiResonse = response.data;

                        if(apiResonse.status !== "True") 
                        {
                            _this.errors = true;
                        }
                        else 
                        {
                            _this.$cookie.set('loggedIn', apiResonse.id, '1Y');
                            _this.$cookie.set('userName', _this.input.username, '1Y');
                            window.location = "/";
                            window.location = "/";
                        }
                    });
                }
            }
        }
    }
</script>