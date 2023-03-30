Splitting();

const options = {
  root: null, // use the document's viewport as the container
  rootMargin: "0px", // % or px - offsets added to each side of the intersection
  threshold: 0.2
};

const itemDelay = 0.1;

let fadeupCallback = (entries, self) => {
  let itemLoad = 0;
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
      tl.set(entry.target, { visibility: "visible" });
      tl.from(entry.target, {
        duration: 1.5,
        y: 200,
        skewY: 40,
        autoAlpha: 0,
        delay: itemLoad * itemDelay,
        ease: "power3.out"
      });
      itemLoad++;
      self.unobserve(entry.target);
    }
  });
};

let fadeupObserver = new IntersectionObserver(fadeupCallback, options);

document.querySelectorAll("h1 span, img").forEach((fadeup) => {
  fadeupObserver.observe(fadeup);
});
