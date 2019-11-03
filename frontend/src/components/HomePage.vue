<template>
    <div class = "row justify-content-center">
        <div class="card" style="width: 36rem;">
            <div class="card-body">
                <router-link :to="{ path: 'anunturi' }" style = "text-decoration:none"><button type="button" class="btn btn-info btn-lg btn-block" style = "height: 36rem; border-radius: .9rem; text-decoration:none;"><span style = "font-size: 36px;">Am nevoie</span></button></router-link>
            </div>
        </div>
        <div class="card" style="width: 36rem; margin-left: 1rem;">
            <div class="card-body">
                <router-link :to="{ path: 'ofer' }" style = "text-decoration:none"><button type="button" class="btn btn-success btn-lg btn-block" style = "height: 36rem; border-radius: .9rem; text-decoration:none;"><span style = "font-size: 36px;">Ofer</span></button></router-link>
            </div>
        </div>
    </div>
</template>