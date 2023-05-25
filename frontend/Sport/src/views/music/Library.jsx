import React, { useState } from 'react'

import { NavLibrary } from './NavLibrary'
import { Songs } from './Songs'
import { Playlists } from './Playlists'


export const Library = ({ 
  listMusic, setListMusic, listPlaylists, setListPlaylists 
}) => {
  
  const [openSongs, setOpenSongs] = useState(false)
  const [openPlaylists, setOpenPlaylists] = useState(false)
  
  return (
    !openSongs && !openPlaylists ? <NavLibrary setOpenSongs={setOpenSongs} setOpenPlaylists={setOpenPlaylists} /> :
    openSongs ? <Songs setOpenSongs={setOpenSongs} listMusic={listMusic} 
    listPlaylists={listPlaylists}
    />
    : openPlaylists ? <Playlists setOpenPlaylists={setOpenPlaylists}
    listPlaylists={listPlaylists} setListPlaylists={setListPlaylists} 
    listMusic={listMusic}
    />
    : null 
  )
}