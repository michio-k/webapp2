import {axios} from '../index.js';

export default {
    getUserId(id) {
        return axios.$get(`users/${id}`)
    },
    getUsers() {
        return axios.$get(`users`)
    }
}