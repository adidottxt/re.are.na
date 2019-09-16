import React, { useContext, useEffect } from "react"
import { gql } from 'apollo-boost'
import { useQuery } from '@apollo/react-hooks'

import Row from '../rows/Row'
import { ContentContext } from './ContentContext'

import '../../css/Content.css'


var requestSent = false;
var setLoading = true;
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

  // wrapper function to set our global bools to true
  // this is done to add empty rows to the context and ensure that
  // we use the new data we receive when loading is set back to false
  function refetchAndReload() {
    setLoading = true;
    requestSent = true;
    refetch();
  }

  useEffect(() => {
    // mark requestSent to true if loading is true (which is set by Apollo)
    if (loading) {
      requestSent = true;
    }

    // if refetchAndReload() is run and the networkStatus is set to 4,
    // add empty rows to signal loading, then refetch() to update UI
    if ((networkStatus === refetchValue) && setLoading) {
      addEmptyRows();
      setLoading = false;
      refetch();
    }

    // if loading is False but a request was sent
    // we have data to update the UI with
    if (!loading && requestSent) {
      var new_data = data.allBlocks.edges.slice(data.allBlocks.edges.length - 3);
      addRows(new_data);
      requestSent = false;
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
