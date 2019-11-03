<template>
    <div class="container">
	<div class="d-flex justify-content-center h-100">
		<div class="card">
			<div class="card-header">
				<h3>Inregistrare</h3>
			</div>
			<div class="card-body">

                <div class="alert alert-danger" role="alert" v-if = "this.status == 'error'">
                    <i class = "fas fa-ban-o"></i> Inregistrarea a esuat!
                </div>

                <div class="alert alert-success" role="alert" v-if = "this.status == 'success'">
                    <i class="fas fa-check-square"></i> Te-ai inregistrat cu success!
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
                <div class="input-group form-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text"><i class="fas fa-envelope-square"></i></span>
                    </div>
                    <input type="email" v-model="input.email" class="form-control" placeholder="Adresa Email">
                </div>
                <div class="input-group form-group">
                    <div class="input-group-prepend">
                        <span class="input-group-text"><i class="fas fa-phone"></i></span>
                    </div>
                    <input type="number" v-model="input.phone" class="form-control" placeholder="Numar telefon">
                </div>
                <div class="form-group">
                    <input type="submit" v-on:click="register()" value="Inregistrare" class="btn float-right btn btn-outline-primary">
                </div>
			</div>
			<div class="card-footer">
				<div class="d-flex justify-content-center links">
					<router-link class="" to="/login">Ai deja cont? Autentifica-te</a></router-link>
				</div>
			</div>
		</div>
	</div>
</div>
</template>

<script>
    import axios from "axios";

    export default {
        name: 'Register',
        data() {
            return {
                input: {
                    username: "",
                    password: "",
                    email: "",
                    phone: ""
                },
                status: "none",
            }
        },
        methods: {
            register() 
            {
                if(this.input.username != "" && this.input.password != "") 
                {                    
                    let _this = this;

                    axios.post("http://vps1.thecodeleones.club/register", {username: this.input.username, password: this.input.password, email: this.input.email, phone_number: this.input.phone}).then(function(response) {
                        let apiResonse = response.data;

                        if(apiResonse.status !== "True") 
                        {
                            _this.status = 'error';
                        }
                        else 
                        {
                            _this.status = 'success';
                            setTimeout(async () => {
                                window.location = '/login';
                            }, 5000);
                        } 
                    });
                }
            }
        }
    }
</script>