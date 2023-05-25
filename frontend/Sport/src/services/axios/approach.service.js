import axios from "axios"
import { myHost } from '../js/url.js'

// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

export const ApproachService = {
  async create(request) {
    const response = await axios.post(`${myHost}/workout/approach/create`, request)

    return response.data
  },

  async delete(request) {
    const response = await axios.post(`${myHost}/workout/approach/delete`, request)

    return response.data
  },

  async edit(request) {
    const response = await axios.post(`${myHost}/workout/approach/update`, request)
  }
}