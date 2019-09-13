import React, { createContext, useState } from 'react';

export const ContentContext = createContext();

const ContentContextProvider = (props) => {
    const [rows, setRows] = useState([
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
      {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
    ])

    const addRows = (new_rows) => {
      setRows(new_rows.map(row => {
          return (
              {
                type: row.node.blockType,
                link: row.node.blockUrl,
                content: row.node.blockContent,
                channel: row.node.channelTitle,
                date: row.node.blockCreateDate,
                title: row.node.blockTitle,
              }
          )
      }))
    }

    const addEmptyRows = (new_rows) => {
      setRows(new_rows.map(row => {
          return (
              {
                type: row.type,
                link: row.link,
                content: row.content,
                channel: row.channel,
                date: row.date,
                title: row.title,
              }
          )
      }))
    }

    return (
      <ContentContext.Provider value={{rows, addRows, addEmptyRows}}>
        {props.children}
      </ContentContext.Provider>
    )
}

export default ContentContextProvider
