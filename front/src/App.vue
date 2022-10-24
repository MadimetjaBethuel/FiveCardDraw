<template>
  <main>
    <h1>Your cards</h1>

    <div class="cards">
      <div v-for="card in cards" class="card">
        <span>{{ card[0] }}</span
        ><br />
        <span>{{ card[1] }}</span
        ><br />
        <span>{{ card[2] }}</span
        ><br />
        <span>{{ card[3] }}</span
        ><br />
        <span>{{ card[4] }}</span
        ><br />
      </div>
    </div>

    <h2>You Hand Rank</h2>

    <p>{{ score }}</p>

    <div class="buttons">
      <button @click="Hand()">get Hand</button>
      <button @click="Score()">get Hand Rank</button>
    </div>
  </main>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      cards: [],
      score: undefined,
    };
  },
  methods: {
    async Hand() {
      const hand = await axios.get("http://127.0.0.1:5000/hand");
      this.cards.push(hand.data.cardData.card);
      console.log(hand.data.cardData);
      console.log(hand.data.cardData.card);
    },
    async Score() {
      const score = await axios.get("http://127.0.0.1:5000/hand");

      this.score = score.data.cardData.score;

      console.log(score.data.cardData.score);
    },
  },
};
</script>

<style scoped>
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  .cards {
    display: flex;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
