import axios from "axios"
import { myHost } from '../js/url.js'

// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

export const WorkoutService = {
  async create(request) {
    const response = await axios.post(`${myHost}/workout/workout/create`, request)

    return response.data
  },

  async delete(request) {
    const response = await axios.post(`${myHost}/workout/workout/delete`, request)

    return response.data
  },

  async edit(request) {
    const response = await axios.post(`${myHost}/workout/workout/update`, request)
  }
}