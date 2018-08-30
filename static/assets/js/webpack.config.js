const path = require('path');
const webpack = require('webpack');
// const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const BUILD_DIR = path.resolve(__dirname, 'dist/');
const APP_DIR = path.resolve(__dirname, 'src');
const {VueLoaderPlugin} = require('vue-loader');

//Build
module.exports = function (env) {
    //Setting env
    const ENV = env.production && 'production' || 'development';

    return {
        mode: ENV,

        entry: {
            index: APP_DIR + '/index.js'
        },
        output: {
            path: BUILD_DIR,
            filename: '[name].bundle.js' // Or [name]
        },
        module: {
            rules: [
                {
                    test: /\.vue$/,
                    loader: 'vue-loader'
                }
            ]
        },
        resolve: {
            extensions: ['.js', '.vue', '.json',],
            modules: [
                path.resolve('./src'),
                path.resolve('./node_modules')
            ], alias: {
                'vue$': 'vue/dist/vue.esm.js'
            }
        },
        plugins: [
            new VueLoaderPlugin(),
            new webpack.DefinePlugin({
                'process.env.NODE_ENV': JSON.stringify(ENV)
            })
        ]
    }
};