/**
 * @Author: andreacasino
 * @Date:   2017-09-15T20:49:07+01:00
 * @Last modified by:   andreacasino
 * @Last modified time: 2017-09-17T20:14:28+01:00
 */

import {Grid, Row, Col} from 'react-bootstrap';
import React,{ Component } from 'react';
import './PalindromeList.css';



class PalindromeList extends Component{

  //Display list of palindromes, fill any empty spots with white space
  displayPalindromes(palindromes){
    var palindromeList = [];
    // eslint-disable-next-line
    var list;
    var counter=0;
    // eslint-disable-next-line
    if(palindromes && palindromes.length>0){
      // eslint-disable-next-line
      list = palindromes.map((palindrome,i)=>{
        palindromeList.push(<Col
                                className='result'
                                key={i}
                                md={6}
                                mdOffset={0}>
                                {palindrome.text}
                            </Col>);
      })
    counter = palindromes.length}

    for (var i = counter; i < 10; i++) {
      palindromeList.push(<Col
                              className='result'
                              key={i}
                              md={6}
                              mdOffset={0}>
                          </Col>);
    }
    return palindromeList
  }

  render(){
    const palindromes = this.props.palindromes;
    return(
      <div id="listContainer">
        <Grid id="resultList">
          <Row>
            {this.displayPalindromes(palindromes)}
          </Row>
        </Grid>
      </div>
    )}}

export default PalindromeList;
