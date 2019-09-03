import React from "react"

import Block from "./Block"
import BlockInfo from "./BlockInfo"

function Row(props) {
    return (
      <div id = 'row'>
            <Block imgsrc={props.imgsrc} linksrc={props.linksrc} />
            <BlockInfo
                title={props.title}
                channel={props.channel}
                date={props.date}
            />
      </div>
    )
}

export default Row
