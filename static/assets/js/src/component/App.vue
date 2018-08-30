<template>
    <section class="panel panel-default">
        <header class="panel-heading">
            <h1>
                Thanks for the opportunity :)
            </h1>
        </header>

        <div v-for="field in fields">
            <form-vue v-bind:fields="field"></form-vue>
        </div>
    </section>
</template>


<script type="text/javascript">
    //Import needed component
    import FormVue from 'component/Form.vue'
    import Settings from 'setting'

    //Return default App class
    export default {
        name: 'app',
        // Bind components
        components: {
            FormVue
        },
        // Get the data
        data() {
            return {
                fields: []
            }
        },
        mounted() {
            this.$http.get(
                // Risk api request
                Settings.rootApi.concat(Settings.allRiskEndPoint)
            ).then(e => {
                if ('data' in e && e.data.length > 0) {
                    this.fields = e.data
                }
            })
        }
    };
</script>
