import axios from "axios"
import { myHost } from '../js/url.js'

// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

export const PlaylistService = {
  async create(request) {
    const response = await axios.post(`${myHost}/music/playlist/create`, request)

    return response.data
  },

  async getAll() {
    const response = await axios.post(`${myHost}/music/playlist/get_all`)

    return response.data.playlists
  },

  async delete(request) {
    const response = await axios.post(`${myHost}/music/playlist/delete`, request)

    return response.data
  },

  async addToPlaylist(request) {
    const response = await axios.post(`${myHost}/music/playlist/add_many_music_to_playlist`, request)
  }
}