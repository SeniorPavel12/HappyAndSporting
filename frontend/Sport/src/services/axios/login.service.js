import axios from "axios"
import { myHost } from '../js/url.js'

export const LoginService = {
  // The user was resitred?
  async isRegister() {
    const response = await axios.post(`${myHost}/refresh_token/`)

    return response.data
  },

  // For a Registration
  async giveTokens(login, pass) {
    const response = await axios.post(`${myHost}/get_pair_token/`, {
      username: login, password: pass
    })
    .then((response) => {
      data = response.data
      localStorage.setItem('accessToken', data.access)
      localStorage.setItem('refresh', data.refresh)
    })
  },

  async createUsers(login, pass) {
    const response = await axios.post(`${myHost}/create_user/`, {
      username: login, password: pass
    })
    .then((response) => {
      data = response.data
      console.log('Create user') // Test
      this.giveTokens(login, pass)
      console.log('Login user') // Test
      console.log(localStorage) // Test
    })
  },

  // For a Logout
  async logoutUser() {
    const response = await axios.post(`${myHost}/path/`) // Add path

    return response.data
  }
}