import React from "react"

import "../css/BlockInfo.css"

function BlockInfo(props) {
  return (
    <div id='info'>
      <div id='title'>
        <p id='channel-info'>title:</p>
        <p id='channel-info-data'>{props.title}</p>
      </div>
      <div id='channel'>
        <p id='channel-info'>channel:</p>
        <p id='channel-info-data'>{props.channel}</p>
      </div>
      <div id='date'>
        <p id='channel-info'>add date:</p>
        <p id='channel-info-data'>{props.date}</p>
      </div>
    </div>
  )
}

export default BlockInfo
