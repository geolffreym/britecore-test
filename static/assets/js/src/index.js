'use strict';
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import App from 'component/App.vue'

// Link router
Vue.use(VueRouter);
//Link resource http
Vue.use(VueResource);


//Setting up router
const router = new VueRouter({
    routes: [{
        path: '/',
        name: 'home',
        component: App
    }]
});


// Setting up app
new Vue({
    router,
    render: createEle => createEle(App)
}).$mount('#main');