import React, { useContext, useEffect, useRef } from "react"
import { gql } from 'apollo-boost'
import { useQuery } from '@apollo/react-hooks'

import Row from '../rows/Row'
import { ContentContext } from './ContentContext'

import '../../css/Content.css'

const refetchValue = 4;
const getBlocksDataQuery = gql`
{
  allBlocks {
    edges {
      node {
        blockContent
        blockId
        blockUrl
        blockType
        blockTitle
        blockCreateDate
        channelTitle
      }
    }
  }
}
`

function Content() {

  const { loading, data, refetch, networkStatus } = useQuery(getBlocksDataQuery, {
    notifyOnNetworkStatusChange: true,
  });
  const { rows, addRows, addEmptyRows } = useContext(ContentContext);

  let requestSent = useRef(false)
  let setLoading = useRef(false)

  // wrapper function to set our global bools to true
  // to add empty rows to the context and
  // to ensure that we use the new data we receive
  function refetchAndReload() {
    setLoading.current = true;
    requestSent.current = true;
    refetch();
  }

  useEffect(() => {
    // mark requestSent to true if loading is true (which is set by Apollo)
    if (loading) {
      requestSent.current = true;
    }

    // if refetchAndReload() is run and the networkStatus is set to 4,
    // add empty rows to signal loading, then refetch() to update UI
    if ((networkStatus === refetchValue) && setLoading.current) {
      addEmptyRows();
      setLoading.current = false;
      refetch();
    }

    // if loading is False but a request was sent
    // we have data to update the UI with
    if (!loading && requestSent.current) {
      var new_data = data.allBlocks.edges.slice(data.allBlocks.edges.length - 3);
      addRows(new_data);
      requestSent.current = false;
    }

  });

  return (
    <>
      {rows.map((row, index) => {
        return (
          <Row
            key={index}
            type={row.type}
            link={row.link}
            content={row.content}
            title={row.title}
            channel={row.channel}
            date={row.date}
          />
        )}
      )}

      <div id='button-div'>
        <button id='button' onClick={() => {
          refetchAndReload();
        }}>Refresh</button>
      </div>
    </>
  )
}

export default Content
