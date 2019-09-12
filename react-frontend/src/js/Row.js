import React from "react"

import MediaRow from "./MediaRow"
import EmptyRow from "./EmptyRow"
import TextRow from "./TextRow"


function Row(props) {
    if (props.type === 'Empty') {
        return (
            <EmptyRow />
        )
    } else if (props.type === 'Media' || props.type === 'Link' || props.type === 'Image' || props.type === 'Attachment') {
        console.log(props.type, 'media');
        return (
            <MediaRow
                imgsrc={props.content}
                linksrc={props.link}
                title={props.title}
                channel={props.channel}
                date={props.date}
            />
        )
    } else if (props.type === 'Text') {
        console.log(props.type, 'text');
        return (
            <TextRow
                text={props.content}
                linksrc={props.link}
                title={props.title}
                channel={props.channel}
                date={props.date}
            />
        )
    }
}

export default Row
