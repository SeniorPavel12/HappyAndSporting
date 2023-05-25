import React, { useState } from "react";

import styles from './Music.module.scss'
import { Navigation } from '/src/components/display/Navigation.jsx'
import { Add } from "./Add";
import { HeadMusic } from '../../components/display/HeadMusic.jsx'
import { Library } from './Library.jsx'
import { PlaylistService } from "../../services/axios/playlist.service";
import { MusicService } from "../../services/axios/music.service";


export const Music = () => {

  const [openAdd, setOpenAdd] = useState(false)
  const [openLibrary, setOpenLibrary] = useState(true)

  const [listMusic, setListMusic] = useState([])
  const [listPlaylists, setListPlaylists] = useState([])

  // const getPlaylist = async () => {
  //   const data = await PlaylistService.getAll()

  //   setListPlaylists(data)
  // }

  // const getMusic = async () => {
  //   const data = await MusicService.getAll()

  //   setListMusic(data)
  // }


  // getPlaylist()
  // getMusic()
  
  return (
    <>
    <div className={styles.container}>
      <HeadMusic setOpenAdd={setOpenAdd} setOpenLibrary={setOpenLibrary} />
      {
        openAdd ? <Add setListMusic={setListMusic} listPlaylists={listPlaylists}
        setListPlaylists={setListPlaylists}
        /> :
        openLibrary ? <Library listMusic={listMusic} setListMusic={setListMusic}
        listPlaylists={listPlaylists} setListPlaylists={setListPlaylists}
        />
        : null
      }
    </div>
    <Navigation />
    </>
  )
}