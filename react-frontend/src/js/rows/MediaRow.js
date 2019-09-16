import React from "react"

import MediaBlock from "../blocks/MediaBlock"
import BlockInfo from "../blocks/BlockInfo"

import "../../css/Row.css"

function MediaRow(props) {
  return (
    <div id='row'>
      <MediaBlock imgsrc={props.imgsrc} linksrc={props.linksrc} />
      <BlockInfo
        title={props.title}
        channel={props.channel}
        date={props.date}
      />
    </div>
  )
}

export default MediaRow
