import axios from "axios"
import { myHost } from '../js/url.js'

// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

export const MusicService = {
  async create(request) {
    const response = await axios.post(`${myHost}/music/music/create`, request)

    return response.data
  },

  async getAll() {
    const response = await axios.post(`${myHost}/music/music/get_all`)

    return response.data.playlists
  },

  async delete(request) {
    const response = await axios.post(`${myHost}/music/music/delete`, request)

    return response.data
  },

  async edit(request) {
    const response = await axios.post(`${myHost}/music/music/update`, request)
  }
}