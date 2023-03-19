import http from './http.service'

export default {
    login(username, password) {
        return http.post('/api/users/token/', {
            username: username,
            password: password
        });
    },

    logout() {
        return http.post('/api/logout');
    },

    refreshToken(refreshToken) {
        return http.post('/api/users/token/refresh/', {
            refresh: refreshToken
        });
    },

    checkExpriedToken(username) {
        return http.get('/api/users/user/' + username)
    }
 }