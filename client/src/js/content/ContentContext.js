import React, { createContext, useState } from 'react';

export const ContentContext = createContext();

// global empty_rows as placeholders for whenever we need to load new data
const empty_rows = [
  {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
  {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
  {type: 'Empty', link: '', content: '', title: '', channel: '', date: ''},
]

const ContentContextProvider = (props) => {
  const [rows, setRows] = useState(empty_rows)

  // set rows to use the data passed in via new_rows
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

  // set rows to use global empty_rows
  const addEmptyRows = () => {
    setRows(empty_rows.map(row => {
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
