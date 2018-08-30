<template>
    <div class="col-md-4">
        <form class="form-row">
            <div v-for="(fields, k) in fields">
                <div class="panel-heading">
                   <h2> {{ k }} </h2>
                </div>
                <div class="panel-body">
                    <div class="form-group field-input" v-for="field in fields">
                        <span class="">{{ field.label }}</span>
                        <input v-bind:type="field.type" class="form-control"/>
                        <small class="text-muted">{{ field.description }}</small>
                    </div>
                    <div class="">
                        <button type="submit" class="btn btn-primary">
                            Submit
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script type="text/javascript">
    export default {
        props: ['fields']
    };
</script>