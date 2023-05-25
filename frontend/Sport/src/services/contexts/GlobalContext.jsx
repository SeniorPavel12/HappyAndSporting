import React, { createContext, useContext, useState } from 'react'



const GlobalContext = createContext()

export const useGlobalContext = () => {
  return useContext(GlobalContext)
}


export const GlobalProvider = ({ children }) => {
  
  const [listGlobalPlaylists, setListGlobalPlaylists] = useState([])

  const [token, setToken] = useState(undefined)
  
  return (
    <GlobalContext.Provider value={{
      listGlobalPlaylists: listGlobalPlaylists,
      setListGlobalPlaylists: setListGlobalPlaylists,
      token: token,
      setToken: setToken
    }}>
      { children }
    </GlobalContext.Provider>
  )
}