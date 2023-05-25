import axios from "axios"
import { myHost } from '../js/url.js'

// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;

export const ExerciseService = {
  async create(request) {
    const response = await axios.post(`${myHost}/workout/exercise/create`, request)

    return response.data
  },

  async delete(request) {
    const response = await axios.post(`${myHost}/workout/exercise/delete`, request)

    return response.data
  },

  async edit(request) {
    const response = await axios.post(`${myHost}/workout/exercise/update`, request)
  }
}