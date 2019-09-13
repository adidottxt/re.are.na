import React from "react"
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from 'react-apollo'

import Header from "./Header"
import HeaderInfo from "./HeaderInfo"
import Content from "./Content"
import ContentContextProvider from "./ContentContext"

import "../css/App.css"

// Apollo Client setup
const client = new ApolloClient({
  uri: 'http://127.0.0.1:5000/graphql'
})


function App() {
  return (
    <ApolloProvider client={client}>
      <>
        <Header />
        <HeaderInfo />
        <ContentContextProvider>
          <Content />
        </ContentContextProvider>
      </>
    </ApolloProvider>
  )
}

export default App
