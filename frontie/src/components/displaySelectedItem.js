import React, {Component} from 'react';


export default class DisplaySelectedItem extends Component{


 

  render(){
  var Thing = this.props.ActuallySelectedItem;
  return (
  Thing !== undefined &&
    <div style={ {border: '1px solid black', width: 'auto'} }>
      You have chosen {Thing.name}.
      <h1>{Thing.name}</h1>
      <p>{Thing.description}</p>
      <p>{Thing.cost_per_hour}</p>
      <p>{Thing.cost_per_day}</p>
      <img src={Thing.image} />

      <form >
        <input  type={'hidden'} value = {Thing.id} name='id' />
        <input type='submit' value = 'Reserve' />
      </form>
    </div>
  )
  }
}